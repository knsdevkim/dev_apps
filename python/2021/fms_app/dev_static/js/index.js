window.addEventListener('DOMContentLoaded', event => {

    // Toggle the side navigation
    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    if (sidebarToggle) {
        // Uncomment Below to persist sidebar toggle between refreshes
        // if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
        //     document.body.classList.toggle('sb-sidenav-toggled');
        // }
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }

});
$ (document).ready(function(){
    $(".details-input-form").show();
        $(".hide").hide();


        $(".btn-details").click(function(){
            $(".details-input-form").show();
            $(".cr-input-form").hide();
            $(".lifecycle-input-form").hide();
            $(".specifications-input-form").hide();
            $(".settings-input-form").hide();

            $(".btn-cr").removeClass("active text-primary");
            $(".btn-lifecycle").removeClass("active text-primary");
            $(".btn-specifications").removeClass("active text-primary");
            $(".btn-settings").removeClass("active text-primary");
            $(".btn-details").addClass("active text-primary")
        });

        $(".btn-cr").click(function(){
            $(".cr-input-form").show(); 
            $(".details-input-form").hide();
            $(".lifecycle-input-form").hide();
            $(".specifications-input-form").hide();
            $(".settings-input-form").hide();

            $(".btn-details").removeClass("active text-primary");
            $(".btn-lifecycle").removeClass("active text-primary");
            $(".btn-specifications").removeClass("active text-primary");
            $(".btn-settings").removeClass("active text-primary");
            $(".btn-cr").addClass("active text-primary")
        });

        $(".btn-lifecycle").click(function(){
            $(".lifecycle-input-form").show(); 
            $(".details-input-form").hide();
            $(".cr-input-form").hide();
            $(".specifications-input-form").hide();
            $(".settings-input-form").hide();

            $(".btn-cr").removeClass("active text-primary");
            $(".btn-specifications").removeClass("active text-primary");
            $(".btn-settings").removeClass("active text-primary");
            $(".btn-details").removeClass("active text-primary");
            $(".btn-lifecycle").addClass("active text-primary")
        });

        $(".btn-specifications").click(function(){
            $(".specifications-input-form").show(); 
            $(".details-input-form").hide();
            $(".cr-input-form").hide();
            $(".lifecycle-input-form").hide();
            $(".settings-input-form").hide();

            $(".btn-cr").removeClass("active text-primary");
            $(".btn-details").removeClass("active text-primary");
            $(".btn-settings").removeClass("active text-primary");
            $(".btn-lifecycle").removeClass("active text-primary");
            $(".btn-specifications").addClass("active text-primary")
        });

        $(".btn-settings").click(function(){
            $(".settings-input-form").show(); 
            $(".details-input-form").hide();
            $(".cr-input-form").hide();
            $(".lifecycle-input-form").hide();
            $(".specifications-input-form").hide();

            $(".btn-cr").removeClass("active text-primary");
            $(".btn-lifecycle").removeClass("active text-primary");
            $(".btn-details").removeClass("active text-primary");
            $(".btn-specifications").removeClass("active text-primary");
            $(".btn-settings").addClass("active text-primary")
        });

        function readFile(input) {
            if (input.files && input.files[0]) {
                var reader = new FileReader();
        
                reader.onload = function(e) {
                var htmlPreview =
                    '<img width="200" src="' + e.target.result + '" />' +
                    '<p>' + input.files[0].name + '</p>';
                var wrapperZone = $(input).parent();
                var previewZone = $(input).parent().parent().find('.preview-zone');
                var boxZone = $(input).parent().parent().find('.preview-zone').find('.box').find('.box-body');
        
                wrapperZone.removeClass('dragover');
                previewZone.removeClass('hidden');
                boxZone.empty();
                boxZone.append(htmlPreview);
                };
        
                reader.readAsDataURL(input.files[0]);
            }
            }
        
            function reset(e) {
            e.wrap('<form>').closest('form').get(0).reset();
            e.unwrap();
            }
        
            $(".dropzone").change(function() {
            readFile(this);
            });
        
            $('.dropzone-wrapper').on('dragover', function(e) {
            e.preventDefault();
            e.stopPropagation();
            $(this).addClass('dragover');
            });
        
            $('.dropzone-wrapper').on('dragleave', function(e) {
            e.preventDefault();
            e.stopPropagation();
            $(this).removeClass('dragover');
            });
        
            $('.remove-preview').on('click', function() {
            var boxZone = $(this).parents('.preview-zone').find('.box-body');
            var previewZone = $(this).parents('.preview-zone');
            var dropzone = $(this).parents('.form-group').find('.dropzone');
            boxZone.empty();
            previewZone.addClass('hidden');
            reset(dropzone);
            });

            // DRIVERS VIEW
            $(document).ready(function(){
                $('.driver-photos').hide();
                $('.driver-documents').hide();
                $('.driver-reminders').hide();
                $('.driver-vehicle-history').hide();

                // DRIVER OVERVIEW
                $('.btn-driver-overview').click(function(){
                    $('.driver-overview-content').show();
                    $('.driver-photos').hide();
                    $('.driver-documents').hide();
                    $('.driver-reminders').hide();
                    $('.driver-vehicle-history').hide();

                    $('.btn-driver-overview').addClass('driver-active');
                    $('.btn-driver-photos').removeClass('driver-active');
                    $('.btn-driver-documents').removeClass('driver-active');
                    $('.btn-driver-reminders').removeClass('driver-active');
                    $('.btn-driver-vehicle-history').removeClass('driver-active');
                });

                // DRIVER PHOTOS
                $('.btn-driver-photos').click(function(){
                    $('.driver-photos').show();
                    $('.driver-overview-content').hide();
                    $('.driver-documents').hide();
                    $('.driver-reminders').hide();
                    $('.driver-vehicle-history').hide();

                    $('.btn-driver-photos').addClass('driver-active');
                    $('.btn-driver-overview').removeClass('driver-active');
                    $('.btn-driver-documents').removeClass('driver-active');
                    $('.btn-driver-reminders').removeClass('driver-active');
                    $('.btn-driver-vehicle-history').removeClass('driver-active');
                })

                // DRIVER DOCUMENTS
                $('.btn-driver-documents').click(function(){
                    $('.driver-documents').show();
                    $('.driver-overview-content').hide();
                    $('.driver-photos').hide();
                    $('.driver-reminders').hide();
                    $('.driver-vehicle-history').hide();

                    $('.btn-driver-documents').addClass('driver-active');
                    $('.btn-driver-overview').removeClass('driver-active');
                    $('.btn-driver-photos').removeClass('driver-active');
                    $('.btn-driver-reminders').removeClass('driver-active');
                    $('.btn-driver-vehicle-history').removeClass('driver-active');
                })

                // DRIVER RENEWAL REMINDERS
                $('.btn-driver-reminders').click(function(){
                    $('.driver-reminders').show();
                    $('.driver-overview-content').hide();
                    $('.driver-photos').hide();
                    $('.driver-documents').hide();
                    $('.driver-vehicle-history').hide();

                    $('.btn-driver-reminders').addClass('driver-active');
                    $('.btn-driver-overview').removeClass('driver-active');
                    $('.btn-driver-photos').removeClass('driver-active');
                    $('.btn-driver-documents').removeClass('driver-active');
                    $('.btn-driver-vehicle-history').removeClass('driver-active');
                })

                $('.btn-driver-vehicle-history').click(function(){
                    $('.driver-reminders').hide();
                    $('.driver-overview-content').hide();
                    $('.driver-photos').hide();
                    $('.driver-documents').hide();
                    $('.driver-vehicle-history').show();

                    $('.btn-driver-reminders').removeClass('driver-active');
                    $('.btn-driver-overview').removeClass('driver-active');
                    $('.btn-driver-photos').removeClass('driver-active');
                    $('.btn-driver-documents').removeClass('driver-active');
                    $('.btn-driver-vehicle-history').addClass('driver-active');
                });


                // VEHICLE VIEW
                $('.vehicle-overview-content').show();
                $('.vehicle-photos-content').hide();
                $('.vehicle-documents-content').hide();
                $('.vehicle-issues-content').hide();
                $('.vehicle-reminders-content').hide();
                $('.vehicle-assignment-content').hide();
                $('.vehicle-location-content').hide();

                $('.btn-vehicle-overview').click(function(){
                    $('.vehicle-overview-content').show();
                    $('.vehicle-photos-content').hide();
                    $('.vehicle-documents-content').hide();
                    $('.vehicle-issues-content').hide();
                    $('.vehicle-reminders-content').hide();
                    $('.vehicle-assignment-content').hide();
                    $('.vehicle-location-content').hide();

                    $('.btn-vehicle-overview').addClass('vehicle-active');
                    $('.btn-vehicle-photos').removeClass('vehicle-active');
                    $('.btn-vehicle-documents').removeClass('vehicle-active');
                    $('.btn-vehicle-issues').removeClass('vehicle-active');
                    $('.btn-vehicle-reminders').removeClass('vehicle-active');
                    $('.btn-vehicle-assignment').removeClass('vehicle-active');
                    $('.btn-vehicle-location').removeClass('vehicle-active');
                });

                $('.btn-vehicle-photos').click(function(){
                    $('.vehicle-overview-content').hide();
                    $('.vehicle-photos-content').show();
                    $('.vehicle-documents-content').hide();
                    $('.vehicle-issues-content').hide();
                    $('.vehicle-reminders-content').hide();
                    $('.vehicle-assignment-content').hide();
                    $('.vehicle-location-content').hide();

                    $('.btn-vehicle-overview').removeClass('vehicle-active');
                    $('.btn-vehicle-photos').addClass('vehicle-active');
                    $('.btn-vehicle-documents').removeClass('vehicle-active');
                    $('.btn-vehicle-issues').removeClass('vehicle-active');
                    $('.btn-vehicle-reminders').removeClass('vehicle-active');
                    $('.btn-vehicle-assignment').removeClass('vehicle-active');
                    $('.btn-vehicle-location').removeClass('vehicle-active');
                })

                $('.btn-vehicle-documents').click(function(){
                    $('.vehicle-overview-content').hide();
                    $('.vehicle-photos-content').hide();
                    $('.vehicle-documents-content').show();
                    $('.vehicle-issues-content').hide();
                    $('.vehicle-reminders-content').hide();
                    $('.vehicle-assignment-content').hide();
                    $('.vehicle-location-content').hide();

                    $('.btn-vehicle-overview').removeClass('vehicle-active');
                    $('.btn-vehicle-photos').removeClass('vehicle-active');
                    $('.btn-vehicle-documents').addClass('vehicle-active');
                    $('.btn-vehicle-issues').removeClass('vehicle-active');
                    $('.btn-vehicle-reminders').removeClass('vehicle-active');
                    $('.btn-vehicle-assignment').removeClass('vehicle-active');
                    $('.btn-vehicle-location').removeClass('vehicle-active');
                })

                $('.btn-vehicle-issues').click(function(){
                    $('.vehicle-overview-content').hide();
                    $('.vehicle-photos-content').hide();
                    $('.vehicle-documents-content').hide();
                    $('.vehicle-issues-content').show();
                    $('.vehicle-reminders-content').hide();
                    $('.vehicle-assignment-content').hide();
                    $('.vehicle-location-content').hide();

                    $('.btn-vehicle-overview').removeClass('vehicle-active');
                    $('.btn-vehicle-photos').removeClass('vehicle-active');
                    $('.btn-vehicle-documents').removeClass('vehicle-active');
                    $('.btn-vehicle-issues').addClass('vehicle-active');
                    $('.btn-vehicle-reminders').removeClass('vehicle-active');
                    $('.btn-vehicle-assignment').removeClass('vehicle-active');
                    $('.btn-vehicle-location').removeClass('vehicle-active');
                })

                $('.btn-vehicle-reminders').click(function(){
                    $('.vehicle-overview-content').hide();
                    $('.vehicle-photos-content').hide();
                    $('.vehicle-documents-content').hide();
                    $('.vehicle-issues-content').hide();
                    $('.vehicle-reminders-content').show();
                    $('.vehicle-assignment-content').hide();
                    $('.vehicle-location-content').hide();

                    $('.btn-vehicle-overview').removeClass('vehicle-active');
                    $('.btn-vehicle-photos').removeClass('vehicle-active');
                    $('.btn-vehicle-documents').removeClass('vehicle-active');
                    $('.btn-vehicle-issues').removeClass('vehicle-active');
                    $('.btn-vehicle-reminders').addClass('vehicle-active');
                    $('.btn-vehicle-assignment').removeClass('vehicle-active');
                    $('.btn-vehicle-location').removeClass('vehicle-active');
                })

                $('.btn-vehicle-assignment').click(function(){
                    $('.vehicle-overview-content').hide();
                    $('.vehicle-photos-content').hide();
                    $('.vehicle-documents-content').hide();
                    $('.vehicle-issues-content').hide();
                    $('.vehicle-reminders-content').hide();
                    $('.vehicle-assignment-content').show();
                    $('.vehicle-location-content').hide();

                    $('.btn-vehicle-overview').removeClass('vehicle-active');
                    $('.btn-vehicle-photos').removeClass('vehicle-active');
                    $('.btn-vehicle-documents').removeClass('vehicle-active');
                    $('.btn-vehicle-issues').removeClass('vehicle-active');
                    $('.btn-vehicle-reminders').removeClass('vehicle-active');
                    $('.btn-vehicle-assignment').addClass('vehicle-active');
                    $('.btn-vehicle-location').removeClass('vehicle-active');
                })

                $('.btn-vehicle-location').click(function(){
                    $('.vehicle-overview-content').hide();
                    $('.vehicle-photos-content').hide();
                    $('.vehicle-documents-content').hide();
                    $('.vehicle-issues-content').hide();
                    $('.vehicle-reminders-content').hide();
                    $('.vehicle-assignment-content').hide();
                    $('.vehicle-location-content').show();

                    $('.btn-vehicle-overview').removeClass('vehicle-active');
                    $('.btn-vehicle-photos').removeClass('vehicle-active');
                    $('.btn-vehicle-documents').removeClass('vehicle-active');
                    $('.btn-vehicle-issues').removeClass('vehicle-active');
                    $('.btn-vehicle-reminders').removeClass('vehicle-active');
                    $('.btn-vehicle-assignment').removeClass('vehicle-active');
                    $('.btn-vehicle-location').addClass('vehicle-active');
                })
            });
});

let total_elements_added = 0;

function createInputElement() {
    const _d = document;
    
    let inputDescriptionElement = _d.createElement('input');
    let labelDescriptionElement = _d.createElement('label');

    let labelBtnDelete = _d.createElement('label');
    let btnDeleteElement = _d.createElement('button');

    let inputQtyElement = _d.createElement('input');
    let labelQtyElement = _d.createElement('label');

    let inputCostElement = _d.createElement('input');
    let labelCostElement = _d.createElement('label');
    
    let brElement = _d.createElement('br');

    // ROW
    let divRow = _d.createElement('div');

    // COL SM 6
    let divDescriptionCol6 = _d.createElement('div');
    let divQtyCol6 = _d.createElement('div');
    let divCostCol6 = _d.createElement('div');
    let divBtnDelete = _d.createElement('div');
    
    let iDeleteElement = _d.createElement('i');

    divRow.setAttribute('class', 'row');

    divDescriptionCol6.setAttribute('class', 'col-sm-5');
    divQtyCol6.setAttribute('class', 'col-sm-3');
    divCostCol6.setAttribute('class', 'col-sm-3');
    divBtnDelete.setAttribute('class', 'col-sm-1');

    labelDescriptionElement.textContent = 'Description';
    labelQtyElement.textContent = 'Qty';
    labelCostElement.textContent = 'Cost';
    labelBtnDelete.textContent = '';

    iDeleteElement.setAttribute('class', 'fa fa-trash');

    inputDescriptionElement.setAttribute('name', 'bp_description');
    inputDescriptionElement.setAttribute('class', 'form-control');
    inputDescriptionElement.setAttribute('placeholder', 'Description');
    inputDescriptionElement.setAttribute('required', true);

    inputQtyElement.setAttribute('name', 'bp_qty');
    inputQtyElement.setAttribute('class', 'form-control');
    inputQtyElement.setAttribute('placeholder', 'Qty');
    inputQtyElement.setAttribute('required', true);
    
    inputCostElement.setAttribute('name', 'bp_cost');
    inputCostElement.setAttribute('class', 'form-control');
    inputCostElement.setAttribute('placeholder', 'Cost Amount');
    inputCostElement.setAttribute('required', true);
    
    btnDeleteElement.setAttribute('class', 'btn btn-danger');

    btnDeleteElement.setAttribute('type', 'button');
    btnDeleteElement.setAttribute('onclick', 'removeElement()');

    btnDeleteElement.appendChild(iDeleteElement);


    
    divDescriptionCol6.append(labelDescriptionElement);
    divDescriptionCol6.append(inputDescriptionElement);

    divQtyCol6.append(labelQtyElement);
    divQtyCol6.append(inputQtyElement);

    divCostCol6.append(labelCostElement);
    divCostCol6.append(inputCostElement);

    divBtnDelete.append(labelBtnDelete);
    divBtnDelete.append(brElement);
    divBtnDelete.append(btnDeleteElement);

    divRow.append(divDescriptionCol6);
    divRow.append(divQtyCol6);
    divRow.append(divCostCol6);
    divRow.append(divBtnDelete);

    total_elements_added += 1;

    _d.querySelector('div[data-input-collection]').appendChild(divRow);
}

let removeElement = () => {
    let child = document.querySelector('div[data-input-collection]');
    total_elements_added = (total_elements_added > 1) ? total_elements_added - 1 : 0;
    child.removeChild(child.childNodes[total_elements_added]);
}