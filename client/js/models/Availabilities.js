import find from "lodash/find";

export function isFullyAvailable(availabilities) {
  return !find(availabilities, (availability) => {
    return availability.quantity <= 0;
  });
}
