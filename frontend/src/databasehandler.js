import $ from 'jquery';
// URL to firebase-db
const Database_url = "https://murat-db-20-default-rtdb.firebaseio.com/"

// function to get all songs from firebase db
export function getAllSongs() {
    let response
    $.ajax({
        url: Database_url + '.json',
        dataType: "json",
        type: 'GET',
        async: false,
        success: function (serverResponse) {
            // console.log(serverResponse)
            response = serverResponse;
        },
        error: function (serverResponse) {
            console.log("Errorlog: Response: ", serverResponse);
            response = serverResponse;
            throw new Error("Error during loading of all songs");
        }
    });
    return response
}