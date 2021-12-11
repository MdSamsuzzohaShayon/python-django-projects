const department = {
    template: `
<div class="container">
    <button type="button" class="btn btn-primary"  data-bs-toggle="modal" data-bs-target="#exampleModal" v-on:click="addClick()">
        Create
    </button>

    <table class="table table-striped table-bordered table-responsive table-success">
        <thead class="table-dark">
            <tr>
                <th scope="col">Department ID</th>
                <th scope="col">Department Name</th>
                <th scope="col">Options</th>
            </tr>
        </thead>
    <tbody>
        <tr v-for="dep in departments">
            <td>{{dep.DepartmentId}}</td>
            <td>{{dep.DepartmentName}}</td>
            <td>
                <button data-bs-toggle="modal" data-bs-target="#exampleModal" v-on:click="editClick(dep)" class="btn btn-primary" > <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16">  <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>  <path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"/> </svg></button>

                <button v-on:click="deleteClick(dep.DepartmentId)" class="btn btn-danger"> <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash" viewBox="0 0 16 16">  <path fill-rule="evenodd" d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"/></svg></button>
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
                    <label for="DepartmentName" class="form-label">Department Name</label>
                    <input type="text" class="form-control" id="DepartmentName" v-model="DepartmentName" placeholder="E. G. Marketing">
                </div>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="button" v-on:click="createClick()" v-if="DepartmentId == 0" class="btn btn-primary">Create</button>
                <button type="button" v-on:click="updateClick()" v-if="DepartmentId != 0" class="btn btn-primary">Update</button>
            </div>
            </div>
        </div>
    </div>
</div>
` ,
    data() {
        return {
            departments: [],
            modalTitle: "",
            DepartmentName: "",
            DepartmentId: 0
        }
    },
    methods: {
        refreshData() {
            axios.get(urls.API_URL + "department")
                .then(response => {
                    console.log("Res- ", response);
                    this.departments = response.data;
                });
        },
        addClick() {
            this.modalTitle = "Add Department";
            this.DepartmentName = "";
            this.DepartmentId = 0;
        },
        createClick() {
            axios.post(urls.API_URL + "department", {
                DepartmentName: this.DepartmentName,
            })
            .then(response => {
                this.refreshData();
                console.log("Create department- ", response);
            });
        },
        editClick(dep) {
            this.modalTitle = "Edit Department";
            this.DepartmentName = dep.DepartmentName;
            this.DepartmentId = dep.DepartmentId;
        },
        updateClick() {
            axios.put(urls.API_URL + "department", {
                DepartmentId: this.DepartmentId,
                DepartmentName: this.DepartmentName,
            })
                .then(response => {
                    this.refreshData();
                    console.log("Create department- ", response);
                });
        },
        deleteClick(id){
            axios.delete(urls.API_URL + "department/"+ id)
                .then(response => {
                    this.refreshData();
                    console.log("Create department- ", response);
                });
        }
    },
    created: function () {
        this.refreshData();
    }
};




