import axios from "axios";
import React, { useEffect, useState } from "react";
import qs from "qs";
import RoomIndex from "./RoomIndex";
import _ from "lodash";
import makeParam from "../generic/Utils";
import { DATEFORMAT } from "./constants";
import { useLocation, useNavigate, useParams } from "react-router-dom";

function RoomIndexOrDetailWithoutQuery() {
  const [rooms, setRooms] = useState([]);
  const [errorMsg, setErrorMsg] = useState(null);
  const { location: location_name } = useParams();
  const navigate = useNavigate();
  const search = useLocation().search.slice(1);
  const query = qs.parse(search);

  const fetchRooms = (dates) => {
    let paramObj = dates ? { params: dates } : {};
    let jsonUrl = `/locations/${location_name}/json/room`;
    setErrorMsg(null);
    axios
      .get(jsonUrl, paramObj)
      .then(({ data: rooms }) => setRooms(rooms))
      .catch(() => setErrorMsg("An error occurred, we'll take a look at it"));
  };

  const reFilter = (filters) => {
    const formattedDates = {
      arrive: filters.dates.arrive.format(DATEFORMAT),
      depart: filters.dates.depart.format(DATEFORMAT),
    };
    var path = `/locations/${location_name}/stay/`;
    fetchRooms(formattedDates);

    let location = {
      pathname: path,
      search: `?${makeParam(formattedDates)}`,
    };

    navigate(location);
  }

  useEffect(() => {
    // Rooms need to be fetched if the page didn't start out with any rooms
    // which happens when going from individual room to list view.
    if (rooms.length === 0) fetchRooms(null);
  }, []);

  return (
    <RoomIndex
      onFilterChange={reFilter}
      location_name={location_name}
      query={query}
      errorMsg={errorMsg}
      rooms={rooms}
    />
  );
}

export default RoomIndexOrDetailWithoutQuery;
