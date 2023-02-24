function prefixWithZero(string, numberOfZeros) {
  var zeros = '';
  for (let i=0; i<numberOfZeros; i++) {
    zeros += '0';
  }
  return zeros + string
}

function formatDayOrMonth(DayOrMonthAsString) {
  string_length = DayOrMonthAsString.length;
  if (string_length < 2) {
    return prefixWithZero(DayOrMonthAsString, 1);
  }
  return DayOrMonthAsString;
}

bookingDate = new Date();
const [day, month, year] = [
  formatDayOrMonth(String(bookingDate.getDate())),
  formatDayOrMonth(String(bookingDate.getMonth() + 1)),
  String(bookingDate.getFullYear()),
]

console.log(day, month, year)