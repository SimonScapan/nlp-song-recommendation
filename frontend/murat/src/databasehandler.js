import $ from 'jquery';
//old url
//const Database_url = "https://cocktailapp-d958.firebaseio.com/"
const Database_url = "https://murat-db-default-rtdb.europe-west1.firebasedatabase.app/"


export function getAllRecipes() {
    let response
    $.ajax({
        url: Database_url + 'songs.json',
        dataType: "json",
        type: 'GET',
        async: false,
        success: function (serverResponse) {
            response = serverResponse;
        },
        error: function (serverResponse) {
            console.log("Response: ", serverResponse);
            response = serverResponse;
            debugger;
            throw new Error("Error during loading of all recipes");
        }
    });
    return response;
}