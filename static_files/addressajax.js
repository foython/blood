function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

document.addEventListener('DOMContentLoaded', ()=>{
    document.querySelector('#id_division').addEventListener('change', function(){
        const id = document.querySelector('#id_division').value;

        url = '/district';
        if (id != null){
            console.log(id);
            getData(url, id)
        }else{
            console.log(id);
        };
    });

    document.querySelector('#id_district').addEventListener('change', function(){
        const dist_id = document.querySelector('#id_district').value;
        upa_url = '/upazila';
        if (dist_id != null){
            console.log(dist_id);
            getupazila(upa_url, dist_id)
        }else{
            console.log(dist_id);
        };
    });
});

function getData(url, id){
    
    fetch(url,{
        method: 'POST',
        headers:{
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'id': id})
        })
        .then((response)=>{
            return response.json()
        })
        .then((data)=>{
            console.log('data', data);
            console.log(Object.values(data)); 
            
                const cols = document.querySelector("#id_district");
                cols.options.length = 0;
                cols.options.add(new Option("District", "District"));
                for(var k in data){
                    cols.options.add(new Option(k, data[k]));
                }
            
            
        })          

}

function getupazila(url, id){
    
    fetch(url,{
        method: 'POST',
        headers:{
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'id': id})
        })
        .then((response)=>{
            return response.json()
        })
        .then((data)=>{
            console.log('data', data);
            console.log(Object.values(data));             
                const cols = document.querySelector("#id_upazila");
                cols.options.length = 0;
                cols.options.add(new Option("Upazila", "Upazila"));
                for(var k in data){
                    cols.options.add(new Option(k, data[k]));
                }            
            
        })          

}
