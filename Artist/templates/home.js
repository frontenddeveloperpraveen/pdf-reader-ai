document.getElementById('fileInput').addEventListener('change', function() {
    var file = this.files[0];
    console.log('Selected file:', file);

    if (file && file.type === 'application/pdf') {
        var form = document.getElementById('uploader')
        var data = new FormData(form)
        data.append('csrfmiddlewaretoken','{{csrf_token}}')

        var xhr = new XMLHttpRequest()
        xhr.open('POST','upload',true)
        xhr.send(FormData)

        console.log('File Uploaded : ', file.name)
    }else{
        alert('Please selete PDF File')
    }

  });