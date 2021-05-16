import './App.css';

function App() {
  return (
    <div className="App">
      <h1>Songtiteleingabe:</h1>
      <input type="text"></input><button>{"Vorschlag generieren"}</button>
      <h1>Songvorschläge:</h1>
      <table>
          <tr>
          <th>Firstname</th>
          <th>Lastname</th>
          <th>Age</th>
        </tr>
        <tr>
          <td>Jill</td>
          <td>Smith</td>
          <td>50</td>
        </tr>
      </table>

    </div>

  );
}

export default App;
