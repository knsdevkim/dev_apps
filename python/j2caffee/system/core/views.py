from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.contrib.auth.views import (
    LoginView,
    LogoutView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count
from django.views.generic import (
    CreateView,
    FormView,
    UpdateView,
    DeleteView,
    ListView,
    TemplateView
)
from .forms import *

# Create your views here.

def order(request, typeoforder):
    context = {}

    context['typeoforder'] = typeoforder

    if 'new_customer' not in request.session:
        get_invoice = InvoiceModel.objects.create(status="not available")
        request.session['invoice_no'] = get_invoice.invoice_no
        request.session['new_customer'] = True
    else:
        get_invoice = InvoiceModel.objects.all().order_by('pk').last()
        request.session['invoice_no'] = get_invoice.invoice_no

    invoice_fk = InvoiceModel.objects.get(invoice_no = request.session['invoice_no'])
    orders = OrderModel.objects.filter(invoice_no = invoice_fk.pk)

    context['orders'] = OrderModel.objects.filter(invoice_no = invoice_fk)
    context['invoice_no'] = request.session['invoice_no']
    context['products'] = ProductsModel.objects.all()
    context['tables'] = TableModel.objects.all()
    context['discounts'] = DiscountModel.objects.all()
    context['context_title'] = 'Order'
    context['orders'] = orders

    total_damage = 0

    if len(orders) > 0:
        for field in orders:
            total_damage += float(field.price) * float(field.qty)

    context['total_purchase'] = total_damage

    return render(request, 'components/create/order.html', context = context)


def takeorder(request, pk, typeoforder):
    context = {}

    invoice_fk = InvoiceModel.objects.get(invoice_no = request.session['invoice_no'])

    get_order = ProductsModel.objects.get(pk = pk)

    if get_order.dough != None:
        if get_order.dough.qty > 0:
            if OrderModel.objects.filter(invoice_no = invoice_fk,\
             product_name = get_order.product_name).exists():
             messages.error(request, 'Menu is already added to customer order.')
            else:
                OrderModel.objects.create(
                    invoice_no = invoice_fk,
                    product_name = get_order.product_name,
                    price = get_order.price if typeoforder == 'resto' else get_order.online_price,
                    qty = 1
                )
                messages.success(request, 'Successfully added to order cart.')
        else:
            messages.error(request, 'Not enough qty to order.')
    else:
        if get_order.qty > 0:
            if OrderModel.objects.filter(invoice_no = invoice_fk,\
             product_name = get_order.product_name).exists():
             messages.error(request, 'Menu is already added to customer order.')
            else:
                OrderModel.objects.create(
                    invoice_no = invoice_fk,
                    product_name = get_order.product_name,
                    price = get_order.price if typeoforder == 'resto' else get_order.online_price,
                    qty = 1
                )
                messages.success(request, 'Successfully added to order cart.')
        else:
            messages.error(request, 'Not enough qty to order.')

    return redirect(reverse('core:createorder', kwargs = {'typeoforder': typeoforder}))


def checkoutorder(request, typeoforder):
    invoice_fk = InvoiceModel.objects.get(invoice_no = request.session['invoice_no'])

    get_total_expense = OrderModel.objects.filter(invoice_no = invoice_fk)

    if len(get_total_expense) > 0:
        price = 0
        qty = 0
        total = 0

        for field in get_total_expense:
            total += float(field.price) * float(field.qty)

        cash = 0 if request.POST.get('cash', 0) == '' else request.POST.get('cash', 0)

        cash_discount = 0

        if request.POST.get('discountperson', '') != '' and request.POST.get('discountlist', '') != '':
            cash_discount = abs((float(int(request.POST.get('discountlist', 0)) / 100) * int(request.POST.get('discountperson', 0)) * total) - total)

        if total > int(cash):
            messages.error(request, 'Cash insufficient.')
        else:
            invoice = InvoiceModel.objects\
            .filter(invoice_no = request.session['invoice_no'])\
            .update(
                cash = total,
                cash_discount = cash_discount,
                discount = request.POST.get('discountlist', 'N/D'),
                discount_person = request.POST.get('discountperson', '0'),
                status = 'paid' if request.user.is_authenticated else 'not paid',
                tableno = request.POST.get('tablelist', ''),
                typeoforder = typeoforder)

            balance = int(cash) - total

            status_message = f'Order checkout. Customer Change: {balance}' if request.user.is_authenticated else 'Order is pending to cash out in cashier.'

            messages.success(request, status_message)

            del request.session['invoice_no']
            del request.session['new_customer']
            request.session.modified
    else:
        messages.error(request, 'Could not checkout without order.')

    return redirect(reverse('core:createorder', kwargs = {'typeoforder': typeoforder}))

@login_required
def paidStatus(request, pk):
    InvoiceModel.objects.filter(pk=pk).update(status='paid')
    messages.success(request, "Order has been paid.")
    return redirect('core:pendingorder')

@login_required
def generatereports(request):
    context = {}
    total = 0

    context['context_title'] = 'Generate Reports'
    context['form'] = GenerateReportsForm
    context['context_total_purchase'] = total

    if request.method == 'POST':
        date_from = request.POST['date_range_from']
        date_to = request.POST['date_range_to']

        generated_model = OrderModel.objects.filter(date__range = (date_from, date_to)).values('product_name', 'qty', 'price').annotate(num_rows = Count('product_name'), total_qty = Sum('qty'), total_price = Sum('price')).order_by()

        if len(generated_model) > 0:
            for order in generated_model:
                total += float(order['price']) * order['total_qty']

        context['object'] = generated_model
        context['date'] = f'Generated From: {date_from} - {date_to}'
        context['context_total_purchase'] = total

    return render(request, 'components/view/generatereports.html', context = context)

@login_required
def expensereports(request):
    context = {}
    total = 0

    context['context_title'] = 'Generate Expense Reports'
    context['form'] = GenerateReportsForm
    context['context_total_purchase'] = total

    if request.method == 'POST':
        date_from = request.POST['date_range_from']
        date_to = request.POST['date_range_to']

        generated_model = ExpenseModel.objects.filter(date__range = (date_from, date_to))

        if len(generated_model) > 0:
            for order in generated_model:
                total += order.price * order.qty

        context['object'] = generated_model
        context['date'] = f'Generated From: {date_from} - {date_to}'
        context['context_total_purchase'] = total

    return render(request, 'components/view/expensereport.html', context = context)

class LoginClassBaseView(LoginView):
    template_name = 'components/login/view.html'
    authentication_form = LoginForm

class LogoutClassBaseView(LogoutView):
    pass

class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = 'components/view/dashboard.html'

class CategoryCreateClassBaseView(LoginRequiredMixin, CreateView):
    template_name = 'components/create/category.html'
    form_class = ProductCategoryForm

    def get_context_data(self, **kwargs):
        kwargs['context_title'] = 'Create Food Category'
        return super(CategoryCreateClassBaseView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Food category created.')
        return super(CategoryCreateClassBaseView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Could not save category at this moment, Try again.')
        return super(CategoryCreateClassBaseView, self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('core:createcategory')

class ProductCreateClassBaseView(LoginRequiredMixin, CreateView):
    template_name = 'components/create/product.html'
    form_class = ProductsForm

    def get_context_data(self, **kwargs):
        kwargs['context_title'] = 'Create Food Menu'
        return super(ProductCreateClassBaseView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Food menu created.')
        return super(ProductCreateClassBaseView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Could not save food menu at this moment, Try again.')
        return super(ProductCreateClassBaseView, self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('core:createproduct')

class ItemQtyUpdateClassBaseView(UpdateView):
    template_name = 'components/update/item.html'
    form_class = ItemForm

    def get_context_data(self, **kwargs):
        kwargs['context_title'] = 'Update Order Qty'
        return super(ItemQtyUpdateClassBaseView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        try:
            order_item = OrderModel.objects.get(pk = self.kwargs[self.pk_url_kwarg])
            fetch_product = ProductsModel.objects.get(product_name = order_item.product_name)
            print(fetch_product.qty)
            if fetch_product.dough != None:
                if int(fetch_product.dough.qty) <= 0:
                    messages.error(self.request, 'Not enough qty to order.')
                    return self.form_invalid(form)
            if int(fetch_product.qty) <= 0:
                messages.error(self.request, 'Not enough qty to order.')
                return self.form_invalid(form)
            else:
                #self.object = form.save()
                messages.success(self.request, 'Successfully update qty.')
        except Exception as e:
            messages.error(self.request, e)
            return self.form_invalid(form)
        return super(ItemQtyUpdateClassBaseView, self).form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_queryset(self):
        return OrderModel.objects.filter(pk = self.kwargs[self.pk_url_kwarg])

    def get_success_url(self):
        return reverse_lazy('core:createorder', kwargs = {
            'typeoforder': self.kwargs['typeoforder']
        })

class ItemDeleteClassBaseView(DeleteView):
    model = OrderModel
    template_name = None

    def get_success_url(self):
        messages.success(self.request, 'Order item removed.')
        return reverse_lazy('core:createorder', kwargs = {'typeoforder': self.kwargs['typeoforder']})

class CategoryClassBaseView(LoginRequiredMixin, ListView):
    template_name = 'components/view/category.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        kwargs['context_title'] = 'Food Category'
        return super(CategoryClassBaseView, self).get_context_data(**kwargs)

    def get_queryset(self):
        return ProductCategoryModel.objects.all()

class ProductsClassBaseView(LoginRequiredMixin, ListView):
    template_name = 'components/view/foodlist.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        kwargs['context_title'] = 'Food Menu'
        return super(ProductsClassBaseView, self).get_context_data(**kwargs)

    def get_queryset(self):
        return ProductsModel.objects.filter(category = self.kwargs['category'])

class InvoiceClassBaseView(LoginRequiredMixin, ListView):
    template_name = 'components/view/invoice.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        kwargs['context_title'] = 'Invoice'
        return super(InvoiceClassBaseView, self).get_context_data(**kwargs)

    def get_queryset(self):
        return InvoiceModel.objects.filter(status="paid")

class PendingOrderClassBaseView(LoginRequiredMixin, ListView):
    template_name = 'components/view/pendingorder.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        kwargs['context_title'] = 'Pending Orders'
        return super(PendingOrderClassBaseView, self).get_context_data(**kwargs)

    def get_queryset(self):
        return InvoiceModel.objects.filter(status="not paid")

class OrdersClassBaseView(LoginRequiredMixin, ListView):
    template_name = 'components/view/orderlist.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        kwargs['context_title'] = 'Purchase Order'

        get_orders = OrderModel.objects.filter(invoice_no = self.kwargs['invoice_no'])

        total = 0

        if len(get_orders) > 0:
            for order in get_orders:
                total += float(order.price) * order.qty

        kwargs['context_total_purchase'] = total

        return super(OrdersClassBaseView, self).get_context_data(**kwargs)

    def get_queryset(self):
        return OrderModel.objects.filter(invoice_no = self.kwargs['invoice_no'])

class ExpenseClassBaseView(LoginRequiredMixin, ListView):
    template_name = 'components/view/expenselist.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        kwargs['context_title'] = 'Expense'
        return super(ExpenseClassBaseView, self).get_context_data(**kwargs)

    def get_queryset(self):
        return ExpenseModel.objects.all()

class ExpenseCreateClassBaseView(LoginRequiredMixin, CreateView):
    template_name = 'components/create/expense.html'
    form_class = ExpenseForm

    def get_context_data(self, **kwargs):
        kwargs['context_title'] = 'Create Expense'
        return super(ExpenseCreateClassBaseView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Expense added.')
        return super(ExpenseCreateClassBaseView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Could not save expense at this moment, Try again.')
        return super(ExpenseCreateClassBaseView, self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('core:createexpense')

class ExpenseDeleteClassBaseView(LoginRequiredMixin, DeleteView):
    model = ExpenseModel
    template_name = None

    def get_success_url(self):
        messages.success(self.request, 'Expense removed.')
        return reverse_lazy('core:expenselist')

class CategoryUpdateClassBaseView(LoginRequiredMixin, UpdateView):
    template_name = 'components/create/category.html'
    form_class = ProductCategoryForm

    def get_context_data(self, **kwargs):
        kwargs['context_title'] = 'Update Category'
        return super(CategoryUpdateClassBaseView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Successfully update.')
        return super(CategoryUpdateClassBaseView, self).form_valid(form)

    def get_queryset(self):
        return ProductCategoryModel.objects.filter(pk = self.kwargs[self.pk_url_kwarg])

    def get_success_url(self):
        return reverse_lazy('core:updatecategory', kwargs = {
            'pk': self.kwargs[self.pk_url_kwarg]
        })

class ProductUpdateClassBaseView(LoginRequiredMixin, UpdateView):
    template_name = 'components/create/product.html'
    form_class = ProductUpdateForm

    def get_context_data(self, **kwargs):
        kwargs['context_title'] = 'Update Food Details'
        return super(ProductUpdateClassBaseView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Successfully update.')
        return super(ProductUpdateClassBaseView, self).form_valid(form)

    def get_queryset(self):
        return ProductsModel.objects.filter(pk = self.kwargs[self.pk_url_kwarg])

    def get_success_url(self):
        return reverse_lazy('core:updatefood', kwargs = {
            'pk': self.kwargs[self.pk_url_kwarg]
        })

class CategoryDeleteClassBaseView(LoginRequiredMixin, DeleteView):
    model = ProductCategoryModel
    template_name = None

    def get_success_url(self):
        messages.success(self.request, 'Category removed.')
        return reverse_lazy('core:foodcategory')

class ProductDeleteClassBaseView(LoginRequiredMixin, DeleteView):
    model = ProductsModel
    template_name = None

    def get_success_url(self):
        messages.success(self.request, 'Item removed.')
        return reverse_lazy('core:foodlist', kwargs = {
            'category': self.kwargs['category']
        })

class ProductLogClassbaseView(LoginRequiredMixin, ListView):
    template_name = 'components/view/productlogs.html'
    context_object_name = 'object'

    def get_queryset(self):
        return ProductsLogModel.objects.filter(product = self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        kwargs['context_title'] = 'View Inventory Logs'
        return super(ProductLogClassbaseView, self).get_context_data(**kwargs)


class ProductLogCreateClassBaseView(LoginRequiredMixin, FormView):
    template_name = 'components/create/product.html'
    form_class = ProductLogForm

    def get_context_data(self, **kwargs):
        kwargs['context_title'] = 'Inventory'
        return super(ProductLogCreateClassBaseView, self).get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        return self.form_valid(self.get_form()) if self.get_form().is_valid() else self.form_invalid(self.get_form())

    def form_valid(self, form):

        product_fk = ProductsModel.objects.get(pk = self.kwargs['pk'])

        new_qty = 0

        if self.request.POST.get('status', '') == 'ADDED':
            new_qty = int(self.request.POST.get('qty', 0)) + product_fk.qty
        elif self.request.POST.get('status', '') == 'REMOVED':
            if product_fk.qty <= int(self.request.POST.get('qty', 0)):
                new_qty = 0
            else:
                new_qty = product_fk.qty - int(self.request.POST.get('qty', 0))

        product_fk.qty = new_qty
        product_fk.save()

        ProductsLogModel.objects.create(
            product = product_fk,
            qty_added = self.request.POST.get('qty', 0),
            status = self.request.POST.get('status', '')
        )

        messages.success(self.request, 'Inventory updated.')

        return super(ProductLogCreateClassBaseView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Form is invalid to process, Try again.')
        return super(ProductLogCreateClassBaseView, self).form_valid(form)

    def get_success_url(self):
        kwargs = {}
        kwargs['pk'] = self.kwargs['pk']
        return reverse_lazy('core:productlog', kwargs = kwargs)



class CreateViewDough(LoginRequiredMixin, CreateView):
    template_name = 'components/create/dough.html'
    form_class = DoughForm

    def get_context_data(self, **kwargs):
        kwargs['context_title'] = 'Create Entity'
        return super(CreateViewDough, self).get_context_data(**kwargs)

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Entity created.')
        return super(CreateViewDough, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Could not save entity item at this moment, Try again.')
        return super(CreateViewDough, self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('core:createdough')

class ListViewDough(LoginRequiredMixin, ListView):
    template_name = 'components/view/dough.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        kwargs['context_title'] = 'Dough'
        return super(ListViewDough, self).get_context_data(**kwargs)

    def get_queryset(self):
        return DoughModel.objects.all()

class DoughLogClassbaseView(LoginRequiredMixin, ListView):
    template_name = 'components/view/doughlogs.html'
    context_object_name = 'object'

    def get_queryset(self):
        return DoughsLogModel.objects.filter(product = self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        kwargs['context_title'] = 'View Inventory Logs'
        return super(DoughLogClassbaseView, self).get_context_data(**kwargs)


class DoughLogCreateClassBaseView(LoginRequiredMixin, FormView):
    template_name = 'components/create/doughlog.html'
    form_class = DoughLogForm

    def get_context_data(self, **kwargs):
        kwargs['context_title'] = 'Dough Inventory'
        return super(DoughLogCreateClassBaseView, self).get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        return self.form_valid(self.get_form()) if self.get_form().is_valid() else self.form_invalid(self.get_form())

    def form_valid(self, form):

        dough_fk = DoughModel.objects.get(pk = self.kwargs['pk'])

        new_qty = 0

        if self.request.POST.get('status', '') == 'ADDED':
            new_qty = int(self.request.POST.get('qty', 0)) + dough_fk.qty
        elif self.request.POST.get('status', '') == 'REMOVED':
            if dough_fk.qty <= int(self.request.POST.get('qty', 0)):
                new_qty = 0
            else:
                new_qty = dough_fk.qty - int(self.request.POST.get('qty', 0))

        dough_fk.qty = new_qty
        dough_fk.save()

        DoughsLogModel.objects.create(
            product = dough_fk,
            qty_added = self.request.POST.get('qty', 0),
            status = self.request.POST.get('status', '')
        )

        messages.success(self.request, 'Dough Inventory updated.')

        return super(DoughLogCreateClassBaseView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Form is invalid to process, Try again.')
        return super(DoughLogCreateClassBaseView, self).form_ivalid(form)

    def get_success_url(self):
        kwargs = {}
        kwargs['pk'] = self.kwargs['pk']
        return reverse_lazy('core:doughlog', kwargs = kwargs)

class DoughUpdateClassBaseView(LoginRequiredMixin, UpdateView):
    template_name = 'components/create/doughlog.html'
    form_class = DoughUpdateForm

    def get_context_data(self, **kwargs):
        kwargs['context_title'] = 'Update Food Details'
        return super(DoughUpdateClassBaseView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Successfully update.')
        return super(DoughUpdateClassBaseView, self).form_valid(form)

    def get_queryset(self):
        return DoughModel.objects.filter(pk = self.kwargs[self.pk_url_kwarg])

    def get_success_url(self):
        return reverse_lazy('core:updatedough', kwargs = {
            'pk': self.kwargs[self.pk_url_kwarg]
        })

class DoughDeleteClassBaseView(LoginRequiredMixin, DeleteView):
    model = DoughModel
    template_name = None

    def get_success_url(self):
        messages.success(self.request, 'Entity removed.')
        return reverse_lazy('core:doughlist')


class TableCreateClassBaseView(LoginRequiredMixin, CreateView):
    template_name = 'components/create/table.html'
    form_class    = TableForm

    def get_context_data(self, **kwargs):
        kwargs['context_title'] = 'Create Table'
        return super(TableCreateClassBaseView, self).get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        return self.form_valid(self.get_form()) if self.get_form().is_valid() else self.form_invalid(self.get_form())

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Table is created!')
        return super(TableCreateClassBaseView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Form is invalid to process, Try again.')
        return super(TableCreateClassBaseView, self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('core:tablecreate')


class TableListClassBaseView(LoginRequiredMixin, ListView):
    template_name = 'components/view/table.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        kwargs['context_title'] = 'Tables'
        return super(TableListClassBaseView, self).get_context_data(**kwargs)

    def get_queryset(self):
        return TableModel.objects.all()


class TableDeleteClassBaseView(LoginRequiredMixin, DeleteView):
    model = TableModel
    template_name = None

    def get_success_url(self):
        messages.success(self.request, 'Table removed.')
        return reverse_lazy('core:tablelist')


class DiscountCreateClassBaseView(LoginRequiredMixin, CreateView):
    template_name = 'components/create/discount.html'
    form_class    = DiscountForm

    def get_context_data(self, **kwargs):
        kwargs['context_title'] = 'Create Discount'
        return super(DiscountCreateClassBaseView, self).get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        return self.form_valid(self.get_form()) if self.get_form().is_valid() else self.form_invalid(self.get_form())

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Discount is created!')
        return super(DiscountCreateClassBaseView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Form is invalid to process, Try again.')
        return super(DiscountCreateClassBaseView, self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('core:discountcreate')


class DiscountListClassBaseView(LoginRequiredMixin, ListView):
    template_name = 'components/view/discount.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        kwargs['context_title'] = 'Discounts'
        return super(DiscountListClassBaseView, self).get_context_data(**kwargs)

    def get_queryset(self):
        return DiscountModel.objects.all()


class DiscountDeleteClassBaseView(LoginRequiredMixin, DeleteView):
    model = DiscountModel
    template_name = None

    def get_success_url(self):
        messages.success(self.request, 'Discount removed.')
        return reverse_lazy('core:discountlist')
