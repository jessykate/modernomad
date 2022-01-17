import React from 'react'
import PropTypes from 'prop-types'
import DateRangeSelector from './DateRangeSelector'
import AvailabilityMatrix from './AvailabilityMatrix'
import { Nav, NavItem, NavLink } from 'react-bootstrap';
import { isFullyAvailable } from '../../models/Availabilities'
import RoomCards from './RoomCards'

export default class RoomIndex extends React.Component {
  static propTypes = {
    rooms: PropTypes.array.isRequired,
    onFilterChange: PropTypes.func.isRequired,
    networkLocation: PropTypes.object
  }

  constructor(props) {
    super(props)
    this.state = {activeKey: 1, showAvailabilityTable: false}
  }

  onDateRangeChange(dates) {
    this.props.onFilterChange({dates: dates})
  }

  handleSelect(selectedKey) {
    this.setState({activeKey: selectedKey})
    if (selectedKey == 1) {
      this.setState({showAvailabilityTable: false})
    } else { this.setState({showAvailabilityTable: true})}
  }

  hasDateQuery() {
    return this.props.query
  }

  displayableRooms() {
    if (this.hasDateQuery()) {
      return _.filter(this.props.rooms, (room) => {
        return isFullyAvailable(room.availabilities)
      })
    } else {
      return this.props.rooms
    }
  }

  render() {
    return (
      <div>
        <div className="date-range-row container">
          <DateRangeSelector
            onChange={this.onDateRangeChange.bind(this)}
            maxLength={this.props.networkLocation ? this.props.networkLocation.maxBookingDays : null}
            inputClass='input-lg'
            {...this.props.query} />
        </div>
        <div className="room-card-container">
          <div className="container">
            <div className="row availability-table-toggle">
              <Nav
                variant="pills"
                className="pull-right"
                activeKey={this.state.activeKey}
                onSelect={this.handleSelect.bind(this)}
              >
                <NavItem title="Room Grid">
                  <NavLink eventKey={1}><i className="fa fa-th"></i></NavLink>
                </NavItem>
                <NavItem title="Availability Matrix">
                  <NavLink eventKey={2}><i className="fa fa-list"></i></NavLink>
                </NavItem>
              </Nav>
            </div>
            {
              !this.state.showAvailabilityTable ?
              <RoomCards
                {...this.props}
                loading={this.props.loading}
                rooms={this.displayableRooms()}
              /> :
              <AvailabilityMatrix
                {...this.props}
                rooms={this.props.rooms}
                query={this.props.query}
                >
              </AvailabilityMatrix>
            }
          </div>
        </div>
      </div>
    )
  }
}
