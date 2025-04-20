import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="logo">
        <Link to="/">
          <span className="logo-text">NumberNinja</span>
        </Link>
      </div>
      <div className="nav-links">
        <Link to="/" className="nav-link active">Home</Link>
        <Link to="/problems" className="nav-link">Browse</Link>
        <Link to="/solved" className="nav-link">Solved</Link>
        <Link to="/favorites" className="nav-link">Favorites</Link>
      </div>
      <div className="nav-actions">
        <Link to="/problems" className="btn primary-btn">Explore Problems</Link>
      </div>
    </nav>
  );
};

export default Navbar;