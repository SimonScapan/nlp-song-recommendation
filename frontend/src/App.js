import React, { useState } from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Route, Link, Switch } from "react-router-dom";
import Autocomplete from '@material-ui/lab/Autocomplete'
import TextField from '@material-ui/core/TextField'
import './App.css';
import { getAllSongs } from "./databasehandler"

let allSongs = Object.values(getAllSongs());

function App() {
  const [selectedSong, setSelectedSong] = useState({ song_title: "" });
  const [suggestionResults, setSuggestionResults] = useState([{ song_title: "" }, { song_title: "" }, { song_title: "" }]);
  Array.min = function (array) {
    return Math.min.apply(Math, array);
  };

  let search = (nameKey, myArray) => {
    for (var i = 0; i < myArray.length; i++) {
      if (myArray[i].song_title === nameKey.song_title) {
        return myArray[i];
      }
    }
  }
  var BreakException = {};
  let getSongSuggestions = (songInformations) => {
    let error = []
    // {angry: 0.15, fear: 0.08, genre: 0, happy: 0, interpret: "['Uli']", …}
    allSongs.forEach(function (song) {
      let sentimentError = 0
      if (song.song_title == songInformations.song_title || song.song_genre !== songInformations.song_genre){
        sentimentError = 100000000000
      } else {
        sentimentError += Math.abs(song.happy - songInformations.happy)
        sentimentError += Math.abs(song.angry - songInformations.angry)
        sentimentError += Math.abs(song.surprise - songInformations.surprise)
        sentimentError += Math.abs(song.sad - songInformations.sad)
        sentimentError += Math.abs(song.fear - songInformations.fear)
      }
      error.push(sentimentError)
    });
    let returnSongs = []
    let inbdexOfSmallestError = 0
    for (let index = 0; index < 3; index++) {
      inbdexOfSmallestError = error.indexOf(Math.min.apply(Math, error));
      returnSongs.push(allSongs.splice(inbdexOfSmallestError, 1)[0])
    }

    return returnSongs

  }

  let generateSuggestionDisplay = () => {
    let currentSongInformations = search(selectedSong, allSongs)
    let songSuggestions = getSongSuggestions(currentSongInformations)
    setSuggestionResults(songSuggestions)
    setSelectedSong({ song_title: "" })
  }

  return (
    <div className="App" style={{textAlign:"center"}}>
      <h1 style={{ textAlign: "center" }}>Songtiteleingabe:</h1>

      <Autocomplete
        id="combo-box-demo"
        options={allSongs}
        getOptionLabel={(option) => option.song_title}
        renderInput={(params) => <TextField {...params} label="Combo box" variant="outlined" />}
        style={{
          width: 300,
          marginLeft: "auto",
          marginRight: "auto"
         }}
        onChange={(e) => { setSelectedSong({ song_title: e.target.innerHTML})  } }
         />
      <button
        onClick={() => { generateSuggestionDisplay() }}
        style={{ marginLeft: "auto",
        marginRight: "auto" }}>
        {"Vorschlag generieren"}
      </button>
      <p style={{ textAlign: "center" }}>Songvorschlag:</p>
      <p style={{ textAlign: "center" }}>{suggestionResults[0].song_title}</p>
      <p style={{ textAlign: "center" }}>{suggestionResults[1].song_title}</p>
      <p style={{ textAlign: "center" }}>{suggestionResults[2].song_title}</p>


    </div>
  );
}

export default App;
