import React from "react";
import image1 from "./image-1.png";
import image from "./image.svg";
import "./style.css";
import vector2 from "./vector-2.svg";
import vector3 from "./vector-3.svg";
import vector4 from "./vector-4.svg";
import vector5 from "./vector-5.svg";
import vector6 from "./vector-6.svg";
import vector from "./vector.svg";

export const Home = () => {
  return (
    <div className="home">
      <div className="div">
        <div className="overlap">
          <div className="overlap-group">
            <img className="image" alt="Image" src={image1} />

            <p className="sharpen-your-mind">
              <span className="text-wrapper">Sharpen your mind with </span>

              <span className="span">NumberNinja</span>

              <span className="text-wrapper">&nbsp;</span>
            </p>
          </div>

          <div className="text-wrapper-2">Home</div>

          <div className="text-wrapper-3">Browse</div>

          <div className="text-wrapper-4">Solved</div>

          <div className="text-wrapper-5">Favorites</div>

          <img className="vector" alt="Vector" src={vector4} />

          <img className="img" alt="Vector" src={vector} />

          <img className="vector-2" alt="Vector" src={image} />

          <img className="vector-3" alt="Vector" src={vector2} />
        </div>

        <div className="div-wrapper">
          <div className="text-wrapper-6">Explore Problems</div>
        </div>

        <p className="p">© 2025 NumberNinja. All rights reserved.</p>

        <div className="text-wrapper-7">About</div>

        <div className="text-wrapper-8">FAQ</div>

        <div className="text-wrapper-9">Contact</div>

        <div className="overlap-2">
          <div className="text-wrapper-10">View Your Favorites</div>
        </div>

        <div className="overlap-3">
          <div className="text-wrapper-11">Explore Problems</div>
        </div>

        <p className="text-wrapper-12">
          Challenge yourself with problems across different categories and
          difficulty levels. Track your progress and improve your skills.
        </p>

        <div className="text-wrapper-13">Categories</div>

        <p className="text-wrapper-14">
          Explore problems in different categories to improve your skills.
        </p>

        <div className="overlap-group-2">
          <div className="text-wrapper-15">Number of Problems</div>

          <div className="text-wrapper-16">Difficulty</div>

          <div className="text-wrapper-17">Topic Categories</div>

          <div className="rectangle" />

          <div className="overlap-4">
            <div className="text-wrapper-18">Beginner</div>
          </div>

          <div className="overlap-5">
            <div className="text-wrapper-19">Intermediate</div>
          </div>

          <div className="overlap-6">
            <div className="text-wrapper-20">Advanced</div>
          </div>

          <div className="overlap-7">
            <div className="text-wrapper-21">Algebra</div>
          </div>

          <div className="overlap-8">
            <div className="text-wrapper-22">Word problems</div>
          </div>

          <div className="overlap-9">
            <div className="text-wrapper-23">Discrete Math</div>
          </div>

          <div className="overlap-10">
            <div className="text-wrapper-24">Arithmetic</div>
          </div>

          <div className="overlap-11">
            <div className="text-wrapper-20">Geometry</div>
          </div>

          <div className="overlap-12">
            <div className="text-wrapper-25">Trignometry</div>
          </div>

          <div className="overlap-13">
            <div className="text-wrapper-26">Calculus</div>
          </div>
        </div>

        <div className="overlap-14">
          <div className="text-wrapper-27">User 1</div>

          <img className="vector-4" alt="Vector" src={vector3} />

          <p className="text-wrapper-28">
            NumberNinja helped me improve my problem-solving skills. The variety
            of problems across different categories is amazing!
          </p>
        </div>

        <div className="overlap-15">
          <div className="text-wrapper-27">User 3</div>

          <img className="vector-4" alt="Vector" src={vector6} />

          <p className="text-wrapper-28">
            NumberNinja helped me improve my problem-solving skills. The variety
            of problems across different categories is amazing!
          </p>
        </div>

        <div className="overlap-16">
          <div className="text-wrapper-27">User 2</div>

          <img className="vector-4" alt="Vector" src={vector5} />

          <p className="text-wrapper-28">
            NumberNinja helped me improve my problem-solving skills. The variety
            of problems across different categories is amazing!
          </p>
        </div>

        <div className="overlap-17">
          <div className="text-wrapper-29">10</div>

          <div className="text-wrapper-30">Problems</div>
        </div>

        <div className="overlap-18">
          <div className="text-wrapper-31">7</div>

          <div className="topic-categories">
            Topic
            <br />
            Categories
          </div>
        </div>

        <div className="overlap-19">
          <div className="text-wrapper-31">3</div>

          <div className="difficulty-levels">
            Difficulty
            <br />
            Levels
          </div>
        </div>

        <div className="overlap-20">
          <div className="text-wrapper-32">100%</div>

          <div className="text-wrapper-33">Free Access</div>
        </div>

        <div className="text-wrapper-34">What our Users Say</div>

        <div className="text-wrapper-35">What our Website Provides</div>
      </div>
    </div>
  );
};
