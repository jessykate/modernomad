import axios from "axios";
import React, { useEffect, useState } from "react";
import qs from "qs";

import BookingForm from "./BookingForm";
import Loader from "../generic/Loader";
import { Link, useLocation, useNavigate, useParams } from "react-router-dom";
import isEmpty from "lodash/isEmpty";
import nl2br from "react-nl2br";
import { isFullyAvailable } from "../../models/Availabilities";
import makeParam from "../generic/Utils";
import { DATEFORMAT } from "./constants";
import moment from "moment";

function RoomDetail({ room: baseRoom, drftBalance, fees }) {
  const [room, setRoom] = useState(baseRoom);
  const [isLoading, setIsLoading] = useState(false);
  const { id, location: locationName } = useParams();
  const search = useLocation().search.slice(1);
  let query = qs.parse(search);
  const navigate = useNavigate();

  const fetchRoom = (filters) => {
    const formattedDates = {};
    if (!isEmpty(filters)) {
      formattedDates["arrive"] = moment(filters.dates.arrive).format(
        DATEFORMAT
      );
      formattedDates["depart"] = moment(filters.dates.depart).format(
        DATEFORMAT
      );
      query = formattedDates;
    }

    const path = `/locations/${locationName}/stay/room/${id}`;
    axios
      .get(`/locations/${locationName}/json/room/${id}`)
      .then(({ data: room }) => {
        setRoom(room);
        setIsLoading(false);
      });

    const urlLocation = {
      pathname: path,
      search: `?${makeParam(formattedDates)}`,
    };

    navigate(urlLocation);
  };

  const isRoomAvailable = () =>
    !isEmpty(query) ? isFullyAvailable(room.availabilities) : false;

  useEffect(() => {
    if (!room) {
      setIsLoading(true);
      fetchRoom({});
    }
  }, []);

  return (
    <Loader loading={isLoading}>
      {!isLoading ? (
        <div className="container room-detail">
          <Link
            to={{
              pathname: `/locations/${locationName}/stay/`,
              search: `?${query}`,
            }}
          >
            <i className="fa fa-chevron-left"></i> Back to Rooms
          </Link>
          <h1>{room.name}</h1>
          <div className="row">
            <div className="col-md-8">
              <div className="room-image-panel">
                <img className="room-image img-responsive" src={room.image} />
                {/*room.img && <ImageCarousel img={room.img} />*/}
              </div>
              <p className="room-summary">{nl2br(room.description)}</p>
            </div>
            <div className="col-md-4">
              <div className="panel">
                <BookingForm
                  fees={fees}
                  room={room}
                  datesAvailable={isRoomAvailable()}
                  onFilterChange={fetchRoom}
                  drftBalance={drftBalance}
                  location_name={locationName}
                  query={query}
                />
              </div>
            </div>
          </div>
        </div>
      ) : null}
    </Loader>
  );
}

export default RoomDetail;
