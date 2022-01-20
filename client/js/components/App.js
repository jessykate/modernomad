import React from "react";
import MuiThemeProvider from "material-ui/styles/MuiThemeProvider";
import { ApolloClient, InMemoryCache, ApolloProvider } from "@apollo/client";

import config from "../../apollo.config";

const client = new ApolloClient({
  uri: config.client.service.url,
  cache: new InMemoryCache(),
});

const App = (props) => (
  <ApolloProvider client={client}>
    <MuiThemeProvider>{props.children}</MuiThemeProvider>
  </ApolloProvider>
);

export default App;
