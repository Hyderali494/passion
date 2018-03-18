$(document).ready(function(){
    $("p").click(function(){
        $(this).hide();
    });

       $(window).on("scroll", function() {
            if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) {
                console.log("Reached Bottom");
				if ($(window).data('ajaxready') === false)
					return;
				$(window).data('ajaxready', false);
                if($("[name='page']").val() != "-1") {
                    page = Number($("[name='page']").val()) + 1;
                    $.ajax({url: '/Products?page=' + String(page),
                            method: 'GET',
                            'success': function(response) {
                                if(response.indexOf('<div') > 0) {
                                    $("div.prd-data").append(response);
									$("[name='page']").val(page);
                                }
                                else {
                                    $("[name='page']").val("-1");
                                }
								$(window).data('ajaxready', true);
                              }
                    });
                }

            }
        });

});
