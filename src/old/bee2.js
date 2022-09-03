"use scrict";

const events = require('events');




class Drone {
  constructor(name, x, y, z) {
    this.name = name;
    this.x = x;
    this.y = y;
    this.z = z;
    this.eE = new events.EventEmitter();
    this.waypoints = []
  }

  init() {
    console.log(this.name, "Ready");

    this.eE.on("take off", async (data) => {
      console.log(this.name, "Taking off");
      await new Promise(resolve => setTimeout(resolve, 1000)); //sleep 
      console.log(this.name, "Airborne");
      this.eE.emit("airborne");
    });


    this.eE.on("take waypoints", async (data = {}) => {
      this.waypoints = [...this.waypoints, ...(data.waypoints || [])];
      console.log(this.name, "Took waypoints, now have", this.waypoints.length);
    });

    this.eE.on("fly to waypoints", async (data = {}) => {
      this.waypoints = [...this.waypoints, ...(data.waypoints || [])];
      if (this.waypoints.length === 0) {
        console.log(this.name, "No more waypoints");
        return;
      };
      const waypoint = this.waypoints.shift();
      console.log(this.name, "Flying to", waypoint);
      await new Promise(resolve => setTimeout(resolve, 5000)); //sleep 
      this.x = waypoint[0];
      this.y = waypoint[1];
      this.z = waypoint[2];
      console.log(this.name, "Got to ", this.x, this.y, this.z);
      this.eE.emit("fly to waypoints");
    });
  }


}

(async () => {
  const myDrone0 = new Drone("drone1", 0, 0, 0);
  myDrone0.init();
  myDrone0.eE.emit("take off");
  myDrone0.eE.emit("take waypoints", {
    waypoints: [[1,1,1], [2,2,2], [3,3,3]]
  });
  myDrone0.eE.on("airborne", ()=>{
    myDrone0.eE.emit("fly to waypoints");  
    setTimeout(()=>{
      myDrone0.eE.emit("take waypoints", {
        waypoints: [[4,4,4]]
      });
    },1000); 
  });

})();



