const employee = {
    template: `
<div class="container">
    <button type="button" class="btn btn-primary"  data-bs-toggle="modal" data-bs-target="#exampleModal" v-on:click="addClick()">
        Create
    </button>

    <table class="table table-striped table-bordered table-responsive table-success">
        <thead class="table-dark">
            <tr>
                <th scope="col">Employee ID</th>
                <th scope="col">Employee Name</th>
                <th scope="col">Department</th>
                <th scope="col">DOJ</th>
                <th scope="col">Options</th>
            </tr>
        </thead>
    <tbody>
        <tr v-for="emp in employees">
            <td>{{emp.EmployeeId}}</td>
            <td>{{emp.EmployeeName}}</td>
            <td>{{emp.Department}}</td>
            <td>{{emp.DateOfJoining}}</td>
            <td>
                <button data-bs-toggle="modal" data-bs-target="#exampleModal" v-on:click="editClick(emp)" class="btn btn-primary" > <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16">  <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>  <path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"/> </svg></button>

                <button v-on:click="deleteClick(emp.EmployeeId)" class="btn btn-danger"> <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash" viewBox="0 0 16 16">  <path fill-rule="evenodd" d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"/></svg></button>
            </td>
        </tr>
    </tbody>
    </table>

    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">{{modalTitle}}</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <div class="mb-3">
                    <label for="name" class="form-label">Employee Name</label>
                    <input type="text" class="form-control" id="name" v-model="EmployeeName" placeholder="Kilyon Mbappe">
                </div>
                <div class="mb-3">
                    <label for="Department" class="form-label">Department</label>
                    <select class="form-control" v-model="Department" >
                        <option v-for="dep in departments" >
                            {{dep.DepartmentName}}
                        </option>
                    </select>
                </div>
                <div class="mb-3">
                    <label for="date" class="form-label">Date of join</label>
                    <input type="date" class="form-control" id="date" v-model="DateOfJoining" >
                </div>
                <div class="mb-3">
                    <img v-bind:src="PhotoPath+PhotoFileName" class="img-thumbnail"  alt="...">
                    <label for="formFileSm" class="form-label">Small file input example</label>
                    <input v-on:change="imageUpload" class="form-control" id="formFileSm" type="file">
                </div>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="button" v-on:click="createClick()" v-if="EmployeeId == 0" class="btn btn-primary">Create</button>
                <button type="button" v-on:click="updateClick()" v-if="EmployeeId != 0" class="btn btn-primary">Update</button>
            </div>
            </div>
        </div>
    </div>
</div>
` ,
    data() {
        return {
            isEditing: false,
            departments: [],
            employees: [],
            modalTitle: "",
            EmployeeId: 0,
            EmployeeName: "",
            Department: "",
            DateOfJoining: "",
            PhotoFileName: "anonymous.png",
            PhotoPath: urls.PHOTO_URL
        }
    },
    beforeMount() {
        window.addEventListener("beforeunload", () => {
            if (!this.isEditing) return
            e.preventDefault()
            // Chrome requires returnValue to be set.
            e.returnValue = ""
        })
    },
    methods: {
        refreshData() {
            axios.get(urls.API_URL + "employee")
                .then(response => {
                    // console.log("Res- ", response);
                    this.employees = response.data;
                });
            axios.get(urls.API_URL + "department")
                .then(response => {
                    // console.log("Res- ", response);
                    this.departments = response.data;
                });
        },
        addClick() {
            this.modalTitle = "Add Employee";
            this.EmployeeId = 0;
            this.EmployeeName = "";
            this.Department = "";
            this.DateOfJoining = "";
            this.PhotoFileName = "anonymous.png";
        },
        createClick() {
            axios.post(urls.API_URL + "employee", {
                EmployeeName: this.EmployeeName,
                Department: this.Department,
                DateOfJoining: this.DateOfJoining,
                PhotoFileName: this.PhotoFileName,
            })
                .then(response => {
                    this.refreshData();
                    console.log("Create Employee- ", response);
                });
        },
        editClick(emp) {
            this.modalTitle = "Edit Employee";
            this.EmployeeId = emp.EmployeeId;
            this.EmployeeName = emp.EmployeeName;
            this.Department = emp.Department;
            this.DateOfJoining = emp.DateOfJoining;
            this.PhotoFileName = emp.PhotoFileName;
        },
        updateClick() {
            axios.put(urls.API_URL + "employee", {
                EmployeeId: this.EmployeeId,
                EmployeeName: this.EmployeeName,
                Department: this.Department,
                DateOfJoining: this.DateOfJoining,
                PhotoFileName: this.PhotoFileName,
            })
                .then(response => {
                    this.refreshData();
                    console.log("Update employee- ", response);
                });
        },
        deleteClick(id) {
            axios.delete(urls.API_URL + "employee/" + id)
                .then(response => {
                    this.refreshData();
                    console.log("Delete employee- ", response);
                });
        },
        imageUpload(event) {
            event.preventDefault();
            let formData = new FormData();
            formData.append('file', event.target.files[0]);
            axios.post(urls.API_URL + "employee/savefile", formData)
                .then(response => {
                    window.preventDefault();
                    this.PhotoFileName = response.data;
                    event.preventDefault();
                    console.log("Upload Image- ", response);
                });
        }
    },
    mounted: function () {
        this.refreshData();
    },

};




