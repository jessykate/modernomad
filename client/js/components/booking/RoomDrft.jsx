import React, { useEffect } from "react";
import RoomDrftIndex from "./RoomDrftIndex";
import RoomDetail from "./RoomDetail";
import gql from "graphql-tag";
import qs from "qs";
import _ from "lodash";
import moment from "moment";
import Loader from "../generic/Loader";
import { useLocation, useNavigate, useParams } from "react-router-dom";
import { useQuery } from "@apollo/client";

const GET_RESOURCES = gql`
  query AllResourcesForLocation($arrive: DateTime!, $depart: DateTime!) {
    allLocations {
      edges {
        node {
          name
          slug
          resources(hasFutureDrftCapacity: true) {
            id
            rid
            name
            image
            defaultRate
            hasFutureDrftCapacity
            acceptDrftTheseDates(arrive: $arrive, depart: $depart)
            availabilities(arrive: $arrive, depart: $depart) {
              date
              quantity
            }
          }
        }
      }
    }
  }
`;

function RoomDrftIndexOrDetail({ children }) {
  const { id } = useParams();
  const navigate = useNavigate();
  const search = useLocation().search.slice(1);
  const query = qs.parse(search);
  const parseFormat = 'MM/DD/YYYY'
  const arrive = query.arrive
    ? moment(query.arrive, parseFormat)
    : moment().startOf("day");
  const depart = query.depart
    ? moment(query.depart, parseFormat)
    : arrive.clone().add(7, "days");
  const { loading, error, data } = useQuery(GET_RESOURCES, {
    variables: { arrive, depart },
  });

  const locationData = () => {
    const queryResults = data.allLocations;
    return queryResults && queryResults.edges.length > 0
      ? queryResults.edges
      : null;
  };

  const allResources = () => {
    const location = locationData();
    return location ? location : [];
  };

  const oneResource = (id) => {
    return _.find(allResources(), { rid: parseInt(id) });
  };

  const reFilter = (filters) => {
    const formattedDates = {
      arrive: moment(filters.dates.arrive).format("MM/DD/YYYY"),
      depart: moment(filters.dates.depart).format("MM/DD/YYYY"),
    };
    let path = "/drft/";

    if (id) {
      path = path + "room/" + id;
    }

    path += `?${new URLSearchParams(formattedDates).toString()}`

    navigate(path);
  };

  const renderSubComponent = () => {
    const sharedProps = {
      onFilterChange: reFilter,
      query,
      loading,
    };

    if (!!children) {
      console.log(loading, data);
      debugger;
      const roomID = children.props.routeParams.id;
      const room = oneResource(roomID);

      if (room) {
        return (
          <RoomDetail {...sharedProps} room={room}>
            {children}
          </RoomDetail>
        );
      } else {
        return null;
      }
    } else {
      return <RoomDrftIndex {...sharedProps} rooms={allResources()} />;
    }
  };

  return (
    <Loader loading={loading}>{loading ? null : renderSubComponent()}</Loader>
  );
}

export default RoomDrftIndexOrDetail;
