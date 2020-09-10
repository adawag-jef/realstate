import { createStore, applyMiddleware } from "redux";
import { composeWithDevTools } from "redux-devtools-extension";
import thunk from "redux-thunk";

import rooReducers from "./reducers";

const initialState = {};
const middleware = [thunk];

const store = createStore(
  rooReducers,
  initialState,
  composeWithDevTools(applyMiddleware(...middleware))
);

export default store;
