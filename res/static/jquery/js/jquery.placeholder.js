function isPlaceholder() {
    var input = document.createElement('input');
    return 'placeholder' in input;
}
$(function() {

    if (!isPlaceholder()) {
        var texts = $('input');
        var len = texts.length;
        for (var i = 0; i < len; i++) {
            var self = texts[i];
            var placeholder = $(self).attr('placeholder');
            if (placeholder != null) {
                $(self).attr('placeholder','');
                $(self).val("");
            }
        }
    }
});