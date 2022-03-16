function change(){
    var forms = document.querySelectorAll('.form')
    for (let i = 0; i< forms.length; i++) {
        var form = forms[i];
        if(form.classList.contains('hide')) {form.classList.remove('hide')}
        else form.classList.add('hide')
      }
}