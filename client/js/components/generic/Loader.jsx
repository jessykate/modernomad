import React from "react";
import Skeleton from "react-loading-skeleton";

function Loader({ loading, children, renderChildren }) {
  return loading ? (
    <>
      <h3>
        <Skeleton />
      </h3>
      <p>
        <Skeleton count={5} />
      </p>
    </>
  ) : children || renderChildren()
}

export default Loader;
