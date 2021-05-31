import $ from 'jquery';

// URL to firebase-db
const Database_url = "https://murat-db-30-default-rtdb.europe-west1.firebasedatabase.app/"

// function to get all songs from firebase db
export function getAllSongs() {
    let response
    $.ajax({
        url: Database_url + '.json',
        dataType: "json",
        type: 'GET',
        async: false,
        success: function (serverResponse) {
            response = serverResponse;
        },
        error: function (serverResponse) {
            console.log("Errorlog: Response: ", serverResponse);
            response = serverResponse;
            throw new Error("Error during loading of all songs");
        },
    });
    return response
}