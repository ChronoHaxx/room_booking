$(document).ready(function() {

    
  for(var k in appointments) {
    console.log(k, appointments[k]);
    console.log(appointments[k].fields.start_time.split(''));
    //finding hour start from json parsed date time
    var hour_start = []
    hour_start.push(appointments[k].fields.start_time.split('')[11]);
    hour_start.push(appointments[k].fields.start_time.split('')[12]);
    hour_start = parseInt(hour_start.join(""));
    //the algorithm to get right time back is to add 8. due to gmt+8 ,thus subtracting 24 if exceeded 24
    
    hour_start += 8;
    hour_start_for24h = hour_start
    if (hour_start > 24){
      hour_start -= 24;
      hour_start_for24h = "0" + hour_start ;
    };
    
    //now the minute_start
    var minute_start = [];
    minute_start.push(appointments[k].fields.start_time.split('')[14]);
    minute_start.push(appointments[k].fields.start_time.split('')[15]);
    minute_start_for24h = minute_start.join("");
    minute_start = parseInt(minute_start.join(""));
    //total for duration calculation
    var total_minute_start = minute_start + (hour_start * 60);
    //same as hour_start algorithm
    var hour_end = [];
    hour_end.push(appointments[k].fields.end_time.split('')[11]);
    hour_end.push(appointments[k].fields.end_time.split('')[12]);
    hour_end = parseInt(hour_end.join(""));
    hour_end += 8;
    if (hour_end >= 24){
      hour_end -= 24;
    };
    minute_end = []
    minute_end.push(appointments[k].fields.end_time.split('')[14]);
    minute_end.push(appointments[k].fields.end_time.split('')[15]);
    minute_end = parseInt(minute_end.join(""));
    var total_minute_end = minute_end + (hour_end * 60);

    var hour24_start = hour_start_for24h + ':' + minute_start_for24h;

    var rooom = appointments[k].fields.rooom
    var durration = total_minute_end - total_minute_start
    var duration_S = toString(durration)
    console.log(hour24_start)
    console.log(hour_start)
    console.log(hour_end)
    console.log(rooom)
    console.log(durration)

    $('#datasets').ready(function() {
      var name = appointments[k].fields.objective;
      var duration = durration * (5 / 3); /*must be in mins*/
      var dur = duration_S;
      var startTime = hour24_start;
  
      /*get the hour*/
      var hour = parseInt(hour24_start) * 100;
      /*get the minutes*/
      var min = hour24_start;
      var res = min.split(":");
      var minute = parseInt(res[1]) / 60 * 100;
      var t = hour + parseInt(minute);
      var screen = parseInt(rooom) * 10;
      $('.timetable .layoutdesign').append("<span class='film' style='top:" + screen + "vh;left:calc(10vw + " + t + "px); width:" + duration + "px' data-start='" + startTime + "'>" + name + " -"+dur+"mins</span>");
    });
   }

  
    $('.layoutdesign').click( ".film", function() {
      $(this).toggleClass("activeFilm");
      $('#deleteFilm').show();
    });
  });
  