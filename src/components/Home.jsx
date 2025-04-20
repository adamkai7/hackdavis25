import React from 'react';
import { Link } from 'react-router-dom';
import Navbar from './Navbar';

const Home = () => {
  return (
    <div className="home">
      <Navbar />
      <div className="main-content">
        <div className="hero-section">
          <div className="hero-text">
            <h1>Sharpen your mind with <span className="highlight">NumberNinja</span></h1>
            <p>Challenge yourself with problems across different categories and difficulty levels. Track your progress and improve your skills.</p>
            <div className="cta-buttons">
              <Link to="/problems" className="btn primary-btn">Explore Problems</Link>
              <Link to="/favorites" className="btn secondary-btn">View Your Favorites</Link>
            </div>
          </div>
        </div>

        <div className="categories-section">
          <h2>Categories</h2>
          <p>Explore problems in different categories to improve your skills.</p>
          
          <div className="problem-filters">
            <div className="filter-section">
              <h3>Topic Categories</h3>
              <div className="filter-options">
                <button className="filter-btn">Algebra</button>
                <button className="filter-btn">Geometry</button>
                <button className="filter-btn">Trigonometry</button>
                <button className="filter-btn">Calculus</button>
                <button className="filter-btn">Arithmetic</button>
                <button className="filter-btn">Word problems</button>
                <button className="filter-btn">Discrete Math</button>
              </div>
            </div>
            
            <div className="filter-section">
              <h3>Difficulty</h3>
              <div className="filter-options">
                <button className="filter-btn">Beginner</button>
                <button className="filter-btn">Intermediate</button>
                <button className="filter-btn">Advanced</button>
              </div>
            </div>
            
            <div className="filter-section">
              <h3>Number of Problems</h3>
              <input type="range" min="1" max="20" defaultValue="5" className="slider" />
            </div>
          </div>
        </div>

        <div className="stats-section">
          <h2>What our Website Provides</h2>
          <div className="stats-container">
            <div className="stat-card">
              <h3>10</h3>
              <p>Problems</p>
            </div>
            <div className="stat-card">
              <h3>7</h3>
              <p>Topic Categories</p>
            </div>
            <div className="stat-card">
              <h3>3</h3>
              <p>Difficulty Levels</p>
            </div>
            <div className="stat-card">
              <h3>100%</h3>
              <p>Free Access</p>
            </div>
          </div>
        </div>

        <div className="testimonials-section">
          <h2>What our Users Say</h2>
          <div className="testimonials-container">
            <div className="testimonial-card">
              <div className="user-info">
                <div className="avatar"></div>
                <h3>User 1</h3>
              </div>
              <p>NumberNinja helped me improve my problem-solving skills. The variety of problems across different categories is amazing!</p>
            </div>
            <div className="testimonial-card">
              <div className="user-info">
                <div className="avatar"></div>
                <h3>User 2</h3>
              </div>
              <p>NumberNinja helped me improve my problem-solving skills. The variety of problems across different categories is amazing!</p>
            </div>
            <div className="testimonial-card">
              <div className="user-info">
                <div className="avatar"></div>
                <h3>User 3</h3>
              </div>
              <p>NumberNinja helped me improve my problem-solving skills. The variety of problems across different categories is amazing!</p>
            </div>
          </div>
        </div>

        <footer>
          <div className="footer-content">
            <p>© 2025 NumberNinja. All rights reserved.</p>
            <div className="footer-links">
              <a href="#">About</a>
              <a href="#">FAQ</a>
              <a href="#">Contact</a>
            </div>
          </div>
        </footer>
      </div>
    </div>
  );
};

export default Home;