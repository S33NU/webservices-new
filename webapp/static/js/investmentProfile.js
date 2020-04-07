(function(){
    
    $('#investmentForm').parsley(); 



})();

function saveInvestmentProfile(){
    if($('#investmentForm').parsley().isValid()){
        console.log("sadasdh");
    }
}