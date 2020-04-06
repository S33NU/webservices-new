(function(){
    

    $.get(CONFIG['host']+"/clients/investment-profile/questions", function(res, status){
        
        if(res.statusCode == 0){
            data = res.data;
            data.sort((a, b) => (a.investqorder > b.investqorder) ? 1 : -1);
            
            generateFormHTML(data);
    
        }else if (res.statusCode == 1){

        }

    });



})();

function generateFormHTML(formData){
    console.log(formData);
    htmlStr = '';

    for(var i=0;i< formData.length;i++) {

        if (formData[i].investqtype == "yes/no" && formData[i].investqselection == "singleselect" && formData[i].investqkey.includes(':')){

        }
        else if (formData[i].investqtype == "yes/no" && formData[i].investqselection == "singleselect" && !formData[i].investqkey.includes(':')){
           htmlStr+=generateRadioButtonHTML(formData[i]);
        }     
        else if(formData[i].investqtype == "text" && formData[i].investqselection == "null"){

        }
        

    }
    $("#investmentForm").prepend(htmlStr);

}

function generateRadioButtonHTML(formdata){
    htmlStr="<div class='form-group row'><div class='col-sm-12 mb-3 mb-sm-0'><label>";
    htmlStr+=formdata.investqorder+"."+formdata.investqname+"</label></br>";
    var values = formdata.values;
    for(var i=0;i<values.length;i++){
        dataArray = values[i].split(":");
        htmlStr+="<input type='radio' name='"+formdata.investqkey+"' value='"+dataArray[1]+"'><label> "+dataArray[0]+" </label>"; 
    }

    htmlStr+="</div></div>";

    return htmlStr;

}

function generateTextHTML(formdata){
    
}

