from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericRelation

import uuid

from datetime import datetime

from apps.media.models import MediaModel, DocumentModel

VEHICLE_TYPE_OPTIONS = [
    ('sedan', 'sedan'),
    ('hatchback', 'hatchback'),
    ('mpv', 'mpv'),
    ('suv', 'suv'),
    ('crossover', 'crossover'),
    ('van', 'van'),
    ('pick-up', 'pick-up'),
    ('hybrid', 'hybrid'),
    ('4 wheel truck', '4 wheel truck'),
    ('6 wheel truck', '6 wheel truck'),
    ('8 wheel truck', '8 wheel truck'),
    ('10 wheel truck', '10 wheel truck')
]

VEHICLE_STATUS_OPTIONS = [
    ('active', _('Active')),
    ('in Active', _('In Active')),
    ('maintenance', _('Maintenance')),
    ('out of service', _('Out of Service'))
]

FUEL_TYPE_OPTIONS = [
    ('gasoline', 'Gasoline'),
    ('diesel', 'Diesel'),
    ('e85', 'E85'),
    ('various ethanol mixtures', 'Various Ethanol Mixtures')
]

PRESENT_YEAR = int(datetime.now().strftime("%Y")) + 1

YEAR_LIST = [(str(_), str(_)) for _ in range(1650, PRESENT_YEAR)]
YEAR_LIST.reverse()

class CharField(models.CharField):
    def __init__(self, *args, **kwargs):
        super(CharField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).lower()

class VehicleModel(models.Model):
    id                = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    vehicle_name      = CharField(max_length = 150, default = '', blank = False, null = False, verbose_name = 'Vechile Name', help_text = 'Enter a nickname to distinguish this vehicle in FMS.')
    vehicle_type      = CharField(max_length = 50, choices = VEHICLE_TYPE_OPTIONS, blank = False, null = False, verbose_name = 'Vehicle Type', help_text = 'Categorized this vehicle.')
    ownership         = CharField(max_length = 150, default = '', blank = False, null = False, verbose_name = 'Ownership')
    area_coverage     = CharField(max_length = 200, default = '', blank = False, null = False, verbose_name = 'Area Coverage')
    position_assign   = CharField(max_length = 200, default = '', blank = False, null = False, verbose_name = 'Position Assign')
    case_capacity     = models.IntegerField(default = 0, blank = False, null = False, verbose_name = 'Case Capacity')
    date_receive      = models.DateField(default = datetime.now, blank = False, null = False, verbose_name = 'Date Receive')
    date_acquired     = models.DateField(default = datetime.now, blank = False, null = False, verbose_name = 'Date Acquired')
    aquisition_cost   = models.FloatField(default = 0.00, blank = False, null = False, verbose_name = 'Aquisition Cost')
    useful_life_month = models.IntegerField(default = 0, blank = False, null = False, verbose_name = 'Useful life in month', help_text = 'Enter in Months.')
    origin            = CharField(max_length = 200, default = '', blank = False, null = False, verbose_name = 'Origin')
    status            = CharField(max_length = 50, choices = VEHICLE_STATUS_OPTIONS, blank = False, null = False, verbose_name = 'Status', help_text = 'Vehicle\'s Status')
    media             = GenericRelation(MediaModel, related_query_name = 'media')
    document          = GenericRelation(DocumentModel, related_query_name = 'document')
    record_created    = models.DateField(auto_now = True)

    @property
    def monthly_depreciation(self) -> float:
        return self.aquisition_cost / self.useful_life_month

    @property
    def yearly_depreciation(self) -> float:
        return self.monthly_depreciation * 12

    @property
    def age_month(self) -> float:
        def days_span(date) -> int:
            start      = datetime.now()
            date_split = date.split('-')
            old_date   = datetime(int(date_split[2]), int(date_split[0]), int(date_split[1]))
            calc_date  = start - old_date
            return calc_date.days
        return days_span(self.date_acquired.strftime('%m-%d-%Y')) / 365 * 12

    @property
    def age_year(self) -> float:
        return self.age_month / 12

    @property
    def accumulated_depreciation(self) -> float:
        return self.monthly_depreciation * self.age_month

    @property
    def book_value(self) -> float: 
        book_value = self.aquisition_cost - self.accumulated_depreciation
        return 0 if book_value < 0 else book_value

    def __str__(self):
        return f'({self.vehicle_type}) {self.vehicle_name}'

    class Meta:
        db_table = 'tbl_vehicles'

class VehicleCrModel(models.Model):
    id                     = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    fk                     = models.OneToOneField(VehicleModel, on_delete = models.CASCADE, related_name = 'fk_cr_rn')
    cr_no                  = models.IntegerField(blank = False, null = False, unique = True, verbose_name = 'CR No.', error_messages = {'unique': 'CR no. is already exists in some other data.'})
    date                   = models.DateField(default = datetime.now, blank = False, null = False, verbose_name = 'Date')
    field_office           = CharField(max_length = 200, default = '', blank = False, null = False, verbose_name = 'Field Office')
    chasis_no              = CharField(max_length = 100, default = '', blank = False, null = False,  unique = True, verbose_name = 'Chasis No.', error_messages = {'unique': 'Chasis no. is already exists in some other data.'})
    engine_no              = CharField(max_length = 100, default = '', blank = False, null = False, unique = True, verbose_name = 'Engine No.', error_messages = {'unique': 'Engine no. is already exists in some other data.'})
    plate_no               = CharField(max_length = 20, default = '', blank = False, null = False, verbose_name = 'Plate No.')
    mvfile_no              = CharField(max_length = 30, default = '', blank = False, null = False, verbose_name = 'MV File No.')
    denomination           = CharField(max_length = 100, default = '', blank = False, null = False, verbose_name = 'Denomination')
    piston_displacement    = CharField(max_length = 100, default = '', blank = False, null = False, verbose_name = 'Piston Displacement')
    no_cyclender           = CharField(max_length = 150, default = '', blank = False, null = False, verbose_name = 'No. Cyclender')
    fuel_type              = CharField(max_length = 50, choices = FUEL_TYPE_OPTIONS, blank = False, null = False, verbose_name = 'Fuel Type')
    make                   = CharField(max_length = 150, default = '', blank = False, null = False, verbose_name = 'Make')
    series                 = CharField(max_length = 150, default = '', blank = False, null = False, verbose_name = 'Series')
    body_type              = CharField(max_length = 100, default = '', blank = False, null = False, verbose_name = 'Body Type')
    body_no                = CharField(max_length = 150, default = '', blank = False, null = False, verbose_name = 'Body No.')
    year_model             = CharField(max_length = 4, choices = YEAR_LIST, blank = False, null = False, verbose_name = 'Year Model')
    gross_weight           = models.FloatField(default = 0, blank = False, null = False, verbose_name = 'Gross Weight')
    net_weight             = models.FloatField(default = 0, blank = False, null = False, verbose_name = 'Net Weight')
    shipping_weight        = models.FloatField(default = 0, blank = False, null = False, verbose_name = 'Shipping Weight')
    net_capacity           = models.IntegerField(default = 0, blank = False, null = False, verbose_name = 'Net Capacity')
    owner                  = CharField(max_length = 150, default = '', blank = False, null = False, verbose_name = 'Owner')
    contact_no             = CharField(max_length = 13, default = '', blank = False, null = False, verbose_name = 'Contact No.')
    address                = CharField(max_length = 250, default = '', blank = False, null = False, verbose_name = 'Address', help_text = '(No., Street, City / Municipality, Province)')
    encumbered             = CharField(max_length = 200, default = '', blank = False, null = False, verbose_name = 'Encumbered')
    details_f_registration = CharField(max_length = 250, default = 'Not Available', blank = False, null = False, verbose_name = 'Details of First Registration')
    amount                 = models.DecimalField(default = 0.00, max_digits = 15, decimal_places = 2, blank = False, null = False, verbose_name = 'Amount')
    record_created         = models.DateField(auto_now = True)

    def __str__(self):
        return str(self.cr_no)

    class Meta:
        db_table = 'tbl_vehicle_cr'

class VehicleOrModel(models.Model):
    id                = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    fk                = models.ForeignKey(VehicleModel, on_delete = models.CASCADE, related_name = 'fk_or_rn')
    or_no             = CharField(max_length = 25, default = '', blank = False, null = False, unique = True, verbose_name = 'OR No.')
    field_office      = CharField(max_length = 250, default = '', blank = False, null = False, verbose_name = 'Field Office')
    field_office_code = CharField(max_length = 200, default = '', blank = False, null = False, verbose_name = 'Field Office Code')
    date              = models.DateField(default = datetime.now, blank = False, null = False, verbose_name = 'Date')
    receive_from      = CharField(max_length = 100, default = '', blank = False, null = False, verbose_name = 'Receive From', help_text = 'Lastname, Firstname, MI.')
    address           = CharField(max_length = 100, default = '', blank = False, null = False, verbose_name = 'Address', help_text = 'No., Street, City / Municipality, Province, Zip Code')
    transaction_no    = CharField(max_length = 100, default = '', blank = False, null = False, verbose_name = 'Transaction No.')
    posted_date       = models.DateField(default = datetime.now, blank = False, null = False, verbose_name = 'Posted Date')
    private           = CharField(max_length = 150, default = '', blank = False, null = False, verbose_name = 'Private')
    file_no           = CharField(max_length = 100, default = '', blank = False, null = False, verbose_name = 'File No.')
    record_created    = models.DateField(auto_now = True)

    def __str__(self):
        return self.or_no

    class Meta:
        db_table = 'tbl_vehicle_or'

class VehicleOrBreakdownPaymentModel(models.Model):
    id          = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    fk          = models.ForeignKey(VehicleOrModel, on_delete = models.CASCADE, related_name = 'fk_orbp_rn')
    description = CharField(max_length = 100, default = '', blank = False, null = False, verbose_name = 'Description')
    qty         = models.PositiveIntegerField(default = 1, blank = False, null = False, verbose_name = 'Qty')
    cost        = models.DecimalField(max_digits = 15, default = '', decimal_places = 2, blank = False, null = False, verbose_name = 'Cost')

    @property
    def total(self):
        return self.cost * self.qty

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'tbl_vehicle_or_breakdown_payment'