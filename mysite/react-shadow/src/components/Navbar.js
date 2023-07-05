import React, { useState } from "react";
import * as FaIcons from "react-icons/fa";
import * as TbIcons from "react-icons/tb";
import * as FiIcons from "react-icons/fi";
import * as GoIcons from "react-icons/go";
import * as GiIcons from "react-icons/gi";
import * as LuIcons from "react-icons/lu";
import { Link } from 'react-router-dom';


// const Home = () => {
const menus = [
    {name: "dashboard", link: '/', icon: TbIcons.TbLayoutDashboard},
    {name: "modules", link: '/', icon: FaIcons.FaList},
    {name: "testruns", link: '/', icon: FaIcons.FaPlay, margin: true},
    {name: "analytics", link: '/', icon: GoIcons.GoGraph},
    {name: "history", link: '/', icon: FaIcons.FaHistory},
    {name: "saved", link: '/', icon: FaIcons.FaRegHeart},
    {name: "config files", link: '/', icon: LuIcons.LuFileJson},
    {name: "user", link: '/', icon: FaIcons.FaUserAstronaut, margin: true},
    {name: "settings", link: '/', icon: FiIcons.FiSettings},
];


function Navbar() {
    const [open, setOpen] = useState(true);
    return (
      <section className="flex gap-6">
        <div className="navbar">
          <div
            className={`bg-[#0e0e0e] min-h-screen ${
              open ? "w-72" : "w-16"
            } duration-500 text-gray-100 px-4`}
          >
            <div className="py-3 flex flex-row justify-auto">
              <Link
                to="#"
                className="menu-bars cursor-pointer"
                size={40}
                onClick={() => setOpen(!open)}
              >
                <GiIcons.GiHangGlider size={40} />
              </Link>
            </div>

                    <div className="mt-4 flex flex-col gap-4 relative">
                        {menus?.map((menu, i) => (
                            <Link
                                to={menu?.link}
                                key={i}
                                className={`${menu?.margin && "mt-8"
                                    } group flex items-center test-sm gap-3 font-medium p-2 hover:bg-gray-800 rounded-lg`}
                            >
                                <div>{React.createElement(menu?.icon, { size: "20", style: { color: "white" } })}</div>
                                <h2
                                    style={{
                                        transitionDelay: `${i + 3}00ms`,
                                    }}
                                    className={`whitespace-pre duration-500 ${!open ? "opacity-0 translate-x-28 overflow-hidden" : ""
                                        }`}
                                >
                                    {menu?.name}
                                </h2>
                                <h2
                                    className={`${open && "hidden"
                                        } absolute left-48 bg-white font-semibold whitespace-pre text-gray-900 rounded-md
                      drop-shadow-lg px-0 py-0 w-0 overflow-hidden group-hover:px-2 group-hover:py-1 
                      group-hover:left-14 group-hover:duration-300 group-hover:w-fit`}
                                >
                                    {menu?.name}
                                </h2>
                            </Link>
                        ))}
                    </div>
          </div>
        </div>
      </section>
    );
}

export default Navbar;