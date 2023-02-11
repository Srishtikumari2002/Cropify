const predict = () => {
    const monthYear = document.getElementById('month').value;
    const date= new Date(monthYear);
    const data = {
        month: date.getMonth(),
        year: date.getFullYear(),
        city: document.getElementById('city').value,
    };

    const responseBox = document.getElementById('respose-container');

    $.ajax({
        url: '/predict',
        type: 'GET',
        data: data,
        success: (res) => {
            console.log(res);
            let content;
            if (res.status == 200) {
                content=`The suggested crop is ${res.crop}.\n\n
                Based on following metrics:\nTemperature: ${res.temperature}
                Humidity: ${res.humidity}
                Rainfall:${res.rainfall}
                Nitrogen:${res.soilComp[0]}
                Phosphorous:${res.soilComp[1]}
                Potassium:${res.soilComp[2]}
                ` 
            } else {
                content = 'We are facing some issues.'
            }
            responseBox.innerText = content;
        },
        error: (error) => {
            console.log(error);
        }
    });

};

window.addEventListener('load', ()=>{
    const date = new Date();
    const year = date.getFullYear();
    const month = ("0"+date.getMonth()).slice(-2);
    document.getElementById('month').value = `${year}-${month}`;
})