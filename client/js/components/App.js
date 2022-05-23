import React from "react";
import { ApolloClient, InMemoryCache, ApolloProvider } from "@apollo/client";

import config from "../../apollo.config";

const client = new ApolloClient({
  uri: config.client.service.url,
  cache: new InMemoryCache(),
});

const App = ({ children }) => (
  <ApolloProvider client={client}>{children}</ApolloProvider>
);

export default App;
