import React, { Component } from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import RoomJoinPage from "./RoomJoinPage";
import CreateRoomPage from "./CreateRoomPage";

export default class HomePage extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <Router>
        <div>
          <nav>
            <ul>
              <li>
                <Link to="/">Home</Link>
              </li>
              <li>
                <Link to="/create">Create Room</Link>
              </li>
              <li>
                <Link to="/join">Join Room</Link>
              </li>
            </ul>
          </nav>

          <Routes>
            <Route path="/" element={<p>This is the home page</p>} />
            <Route path="/create" element={<CreateRoomPage />} />
            <Route path="/join" element={<RoomJoinPage />} />
          </Routes>
        </div>
      </Router>
    );
  }
}