/*
 * Example 2:
 *
 * - default gradient
 * - listening to `circle-animation-progress` event and display the animation progress: from 0 to 100%
 */
$('.python.circle').circleProgress({
  value: 0.8
}).on('circle-animation-progress', function(event, progress) {
  $(this).find('strong').html(parseInt(80 * progress) + '<i>%</i>');
});

$('.django.circle').circleProgress({
  value: 0.65
}).on('circle-animation-progress', function(event, progress) {
  $(this).find('strong').html(parseInt(65 * progress) + '<i>%</i>');
});

$('.elastic.circle').circleProgress({
  value: 0.54
}).on('circle-animation-progress', function(event, progress) {
  $(this).find('strong').html(parseInt(54 * progress) + '<i>%</i>');
});
