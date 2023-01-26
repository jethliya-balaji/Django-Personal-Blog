document.addEventListener("DOMContentLoaded", function (event) {
  console.log("id : id_body");
  let script = document.createElement('script');
  script.setAttribute('src', 'https://cdn.tiny.cloud/1/no-api-key/tinymce/6/tinymce.min.js');
  script.setAttribute('referrerpolicy', 'origin');
  document.head.appendChild(script);

  script.onload = () => {
    tinymce.init({
      selector: '#id_body',
      plugins: 'print preview importcss tinydrive searchreplace autolink autosave save directionality visualblocks visualchars fullscreen image link media template codesample table charmap hr pagebreak nonbreaking anchor toc insertdatetime advlist lists  wordcount imagetools textpattern noneditable help charmap quickbars emoticons blockquote',
      menubar: 'file edit view insert format tools table tc help',
      toolbar: 'undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | a11ycheck ltr rtl | showcomments addcomment',
      autosave_ask_before_unload: true,
      autosave_interval: '30s',
      autosave_prefix: '{path}{query}-{id}-',
      autosave_restore_when_empty: false,
      autosave_retention: '2m',
      image_advtab: true,
      automatic_uploads: false,
      importcss_append: true,
      height: 600,
      image_caption: true,
      quickbars_selection_toolbar: 'bold italic | quicklink h2 h3 blockquote quickimage quicktable',
      noneditable_noneditable_class: 'mceNonEditable',
      toolbar_mode: 'sliding',
      spellchecker_ignore_list: ['Ephox', 'Moxiecode'],
      tinycomments_mode: 'embedded',
      content_style: '.mymention{ color: gray; }',
      contextmenu: 'link image in',
      a11y_advanced_options: true,
      mentions_selector: '.mymention',
      mentions_item_type: 'profile',
      init_instance_callback: function (editor) {
        editor.dom.addClass(editor.dom.select('img'), 'img-fluid');
      }
    });
  }
});