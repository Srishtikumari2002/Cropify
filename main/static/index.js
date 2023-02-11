const predict = ()=>{
    const data = {
        month: document.getElementById('month').ariaValueText,
        city: document.getElementById('city').ariaValueText,
        state: document.getElementById('state').ariaValueText
    };

    const responseBox = document.getElementById('respose-container');

    $.ajax({
        url: window.location.href+'/predict',
        type:'GET',
        data: data,
        success: (res)=>{
            console.log(res);
            responseBox.innerText = res;
        },
        error: (error)=>{
            console.log(error);
        }
    });

};