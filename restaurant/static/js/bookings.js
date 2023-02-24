const pre = document.getElementById('bookings');
const p = document.createElement('p');
var content = document.createTextNode('')

const parse_content = '{{ bookings|safe }}';
if (parse_content === 'No Booking') {
  content = document.createTextNode(parse_content);
  pre.appendChild(p.appendChild(content));
} else {
  const bookings = JSON.parse('{{ bookings|safe }}');

  for (let idx in bookings) {
    let p = document.createElement('p');
    p.appendChild(document.createTextNode(bookings[idx]['fields']['first_name']));
    p.appendChild(document.createTextNode(bookings[idx]['fields']['reservation_time']));
    p.appendChild(document.createTextNode(bookings[idx]['fields']['reservation_slot']));
  }
}
