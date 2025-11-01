function uploadpic(image){
            if(image.files && image.files[0]){
                const file = image.files[0];
                const img = document.getElementById('pic');
                img.src = URL.createObjectURL(file);
            }
        }
