let weather={
    "apiKey":"f8ea6a8f06c75b393085bb7bd20b84f8",
    fetchWeather: function(city){
        fetch(
            "https://api.openweathermap.org/data/2.5/weather?q="
             + city 
             + "&appid=" 
             + this.apiKey,

        )
        .then((response) => {
            if (!response.ok) {
              alert("No weather found.");
              throw new Error("No weather found.");
            }
            return response.json();
          })
        .then((data)=>this.displayWeather(data));
    },
    displayWeather: function(data){
        const { name }=data;
        const{ icon,description }=data.weather[0];
        const { temp, humidity }=data.main;
        const{ speed }=data.wind;
       // console.log(name , icon, description,temp,humidity, speed);
     document.querySelector(".city").innerText="Weather in "+name;
      document.querySelector(".icon").src="http://openweathermap.org/img/wn/" + icon + ".png";
      document.querySelector(".decription").innerText=description;
      document.querySelector(".temp").innerText = temp + "°C";
      document.querySelector(".humidity").innerText="Humidity: " + humidity + "%";
      document.querySelector(".wind").innerText="Wind Speed: " + speed + "km/h";
     document.querySelector(".weather").classList.remove("loading");
     document.body.style.backgroundImage =
     "url('https://source.unsplash.com/1600x900/?" + name + "')";

    },
    search: function(){
       this.fetchWeather( document.querySelector(".search-bar").value);

    },
};
document
.querySelector(".search button")
.addEventListener('click', function(){
 weather.search();

});
document.querySelector(".search-bar").addEventListener("keyup", function(event){
    if(event.key=="Enter"){
        weather.search();
    }
});
weather.fetchWeather("Denver");
