import React, { useState } from 'react';
import NavBar from './NavBar';

const App = () => {
  const [state, setState] = useState();

  const get_quote = (symbol) => {
    let url = `https://finance.yahoo.com/quote/${symbol}`

    fetch(url)
    .then(res => res.text())
    .then(res => {
      console.log(res.body)
      let delimiter = '"QuoteSummaryStore":{';

      let quote = res.split(delimiter)[1] // Trim to the start
      quote = quote.split('(this)')[0] // Trim the gargabe at the end
      quote = quote.substring(0, quote.len - 1 - 3);
      quote = quote.split(`,"symbol":"${symbol}","esgScores":`)[0];
      quote = '{' + quote + '}'
    
      setState(JSON.parse(quote));
    });
  }

  return (
    <div className="App">
      <NavBar />
      {get_quote('MSFT')}
      {JSON.stringify(state)}
    </div>
  );
}

export default App;
