jQuery(document).ready(
    function($) {
	$("#propertyform").dirty_form();
	$("#propertyform a:not(.wikitoolbar a):not(#modify-tabs a)").dirty_stopper();
    });
