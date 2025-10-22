function updatepins(value){ 
            document.getElementById('volumeValue').textContent =  `pins:- ${value} pins`;
        }
function updateliwt(value){
            document.getElementById('line-wt').textContent = `li-wt:- ${value} line-width`;
        }
function updatemxli(value){
            document.getElementById('mx-line').textContent = `mx-li: ${value} max lines`;
        }
function uploadpic(image){
            if(image.files && image.files[0]){
                const file = image.files[0];
                const img = document.getElementById('pic');
                img.src = URL.createObjectURL(file);
            }
        }
