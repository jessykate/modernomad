import React from "react";
import Skeleton from "react-loading-skeleton";

function Loader({ loading, children }) {
  return loading ? (
    <>
      <h3>
        <Skeleton />
      </h3>
      <p>
        <Skeleton count={5} />
      </p>
    </>
  ) : (
    children
  );
}

export default Loader;
