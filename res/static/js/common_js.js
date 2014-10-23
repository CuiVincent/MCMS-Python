function doAjaxCommit( url, param, onSuccess,onError) {
    jQuery.ajax({
        type: "POST",
        url: url,
        data: param,
        contentType: "application/x-www-form-urlencoded;charset=UTF-8",
        dataType: 'json',
        beforeSend: function(xhr) {xhr.setRequestHeader("__IS_AJAX_REQUEST", "true");},
        success: function (result) {
            if (result.success) {
                onSuccess(result);
            } else {
                onError(result);
            }
        },error: function (result) {
            onError(result);
        }
    });
}

function doAjaxCommitForm( url, form, onSuccess,onError) {
    var param = "";
    var queryStr = getQueryStrFomForm(form[0]);
    if (queryStr != undefined) {
        param = queryStr;
    }
    doAjaxCommit( url, param, onSuccess,onError);
}

/**
 * 替换字符中的url特殊字符为标准字符：
 * @return 返回替换之后的字符串
 */
String.prototype.toUrlString=function()
{
    return this.replace(/\%/g,"%25").replace(/\//g,"%2F").replace(/\?/g,"%3F").replace(/\+/g,"%2B").replace(/\#/g,"%23").replace(/\&/g,"%26");
};

/**
 * 字符串不区分大小写的比较
 * @param arg 要比较的字符串
 * @return 如果相同返回true，否则返回false
 */
String.prototype.equalsIgnoreCase=function(arg)
{
    return (new String(this.toLowerCase())==(new String(arg)).toLowerCase());
};


function getQueryStrFomForm(fm)
{
    var tp = fm.elements;
    var str = "";
    var names = "";

    for(var i=0;i<tp.length;i++)
    {
        if(tp[i].type.equalsIgnoreCase("text") || tp[i].type.equalsIgnoreCase("hidden") || tp[i].type.equalsIgnoreCase("textarea") || tp[i].type.equalsIgnoreCase("select-one") || tp[i].type.equalsIgnoreCase("password"))
        {

            if (tp[i].name != "")
            {
                //names = names + "," + tp[i].name;
                str = str + "&" + tp[i].name + "=" + tp[i].value.toUrlString();
            }
        }
        else if ((tp[i].type.equalsIgnoreCase("checkbox") || tp[i].type.equalsIgnoreCase("radio")) && tp[i].checked)
        {

            if (tp[i].name != "")
            {
                str = str + "&" + tp[i].name + "=" + tp[i].value.toUrlString();
            }
        }
    }
    if(str != "")
    {
        str = str.substring(1,str.length);
    }
    return str;
}