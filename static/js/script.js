$(document).ready(function() {
    function fetchWeather() {
        $.get('/weather', function(data) {
            let weatherTable = $('#weatherTable');
            weatherTable.empty();  // Clear the table before adding new data
            data.forEach(function(weather) {
                weatherTable.append(
                    `<tr>
                        <td>${weather.city}</td>
                        <td>${weather.temp}</td>
                        <td>${weather.feels_like}</td>
                        <td>${weather.main}</td>
                        <td>${weather.timestamp}</td>
                    </tr>`
                );
            });
        });
    }

    $('#fetchWeather').click(fetchWeather);
    fetchWeather();  // Fetch weather data when the page loads
});
