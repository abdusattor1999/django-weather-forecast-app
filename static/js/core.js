
var arr = ["Martin", "James", "Jamie", "Jameson", "Jamelia", "Jamela", "StackOverflow"];

$('#query').on({
    "focus": function() {
    $(this).parent().css('border-color', '#CCCCCC');
  },
  "blur": function() {
    $(this).parent().css('border-color', '#EEEEEE');
  },
  "keyup": function() {
    var results = [];
        var val = $(this).val();
    var $queryResults = $('#query-results');
    var queryResultsMarkup = "";

    if (val.length > 1) {
            $queryResults.html("").hide();
            $.each(arr, function(i) {
                if (arr[i].match(new RegExp(val,'i'))) {
                    var $li = $('<li/>')
                        .html(arr[i])
                    .attr('data-value', arr[i]);
                $queryResults.append($li).show();
            }
        });

        $('li').on('click', function() {
            var selectedVal = $(this).attr('data-value');
            $('#query').val(selectedVal);
            $('#query-results').html("").hide();
        });
    } else {
            $queryResults.html("").hide();
    }
  }
});
