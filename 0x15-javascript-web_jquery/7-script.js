$.get('https://swapi.dev/api/people/5/?format=json', function (data) {
  $('DIV#character').text(data.name);
});
