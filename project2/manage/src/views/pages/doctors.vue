<template>
    <div class="fater-body-show">
        <el-card shadow="never">
			<div slot="header">
				信息查询
			</div>
			<div>
				<el-form :inline="true" :model="qryForm">
					<el-form-item >
						<el-input v-model="qryForm.name" placeholder="输入医师姓名…" autocomplete="off"></el-input>
					</el-form-item>
					<el-form-item >
						<el-input v-model="qryForm.phone" placeholder="输入联系电话…" autocomplete="off"></el-input>
					</el-form-item>
					<el-form-item >
						<el-input v-model="qryForm.record" placeholder="输入医师学历…" autocomplete="off"></el-input>
					</el-form-item>
					<el-form-item >
						<el-input v-model="qryForm.job" placeholder="输入医师职称…" autocomplete="off"></el-input>
					</el-form-item>
					<el-form-item>
						<el-button type="primary" icon="el-icon-search" @click="getPageInfo(1, 10)"></el-button>
					</el-form-item>
				</el-form>
			</div>
		</el-card>
		
		<el-card shadow="never">
			<div slot="header">
				<el-button type="primary" size="mini"
						icon="el-icon-plus" @click="showAddWin()"></el-button>
			</div>
			<div>
				<el-table v-loading="loading" 
					element-loading-text="拼命加载中" element-loading-spinner="el-icon-loading"
					element-loading-background="rgba(124, 124, 124, 0.8)" :data="pageInfos" border>
						<el-table-column align="center" type="index"></el-table-column>
						<el-table-column align="center" prop="userName" label="医师账号"></el-table-column>
						<el-table-column align="center" prop="name" label="医师账号"></el-table-column>
						<el-table-column align="center" prop="gender" label="医师性别"></el-table-column>
						<el-table-column align="center" prop="phone" label="联系电话"></el-table-column>
						<el-table-column align="center" prop="record" label="医师学历"></el-table-column>
						<el-table-column align="center" prop="job" label="医师职称"></el-table-column>
						<el-table-column align="center" prop="officeName" label="所属科室"></el-table-column>
						<el-table-column align="center" label="操作处理">
							<template slot-scope="scope">
								<el-button  icon="el-icon-edit"
										type="primary" size="mini" @click="showUpdWin(scope.row)"></el-button>
								<el-button icon="el-icon-delete"
									type="danger" size="mini" @click="delInfo(scope.row.id)"></el-button>
							</template>
						</el-table-column>
				</el-table>
				<el-pagination v-if="pageTotal > 1" style="margin-top: 15px;" @size-change="handleSizeChange"
					@current-change="handleCurrentChange" :current-page="pageIndex" :page-sizes="[10, 20, 50]"
					:page-size="pageSize" layout="total, sizes, prev, pager, next, jumper" :total="totalInfo">
				</el-pagination>
			</div>
        </el-card>
		
		<el-dialog title="添加信息" width="750px" :visible.sync="showAddFlag">
			<el-form label-width="90px" :model="doctorsForm">
				<el-row :gutter="15">
					<el-col :span="12">
						<el-form-item label="医师账号">
							<el-input v-model="doctorsForm.userName" 
										placeholder="请输入医师账号…" autocomplete="off"></el-input>
						</el-form-item>
					</el-col>
					<el-col :span="12">
						<el-form-item label="登陆密码">
							<el-input v-model="doctorsForm.passWord" 
									type="password"	placeholder="请输入医师登陆密码…" autocomplete="off"></el-input>
						</el-form-item>
					</el-col>
				</el-row>
				<el-row :gutter="15">
					<el-col :span="12">
						<el-form-item label="医师姓名">
							<el-input v-model="doctorsForm.name" 
										placeholder="请输入医师姓名…" autocomplete="off"></el-input>
						</el-form-item>
					</el-col>
					<el-col :span="12">
						<el-form-item label="医师年龄">
							<el-input v-model="doctorsForm.age" 
									placeholder="请输入医师年龄…" autocomplete="off"></el-input>
						</el-form-item>
					</el-col>
				</el-row>
				<el-row :gutter="15">
					<el-col :span="12">
						<el-form-item label="联系电话">
							<el-input v-model="doctorsForm.phone" 
										placeholder="请输入联系电话…" autocomplete="off"></el-input>
						</el-form-item>
					</el-col>
					<el-col :span="12">
						<el-form-item label="医师性别">
							<el-radio-group v-model="doctorsForm.gender">
								<el-radio label="男"></el-radio>
								<el-radio label="女"></el-radio>
							</el-radio-group>
						</el-form-item>
					</el-col>
				</el-row>
				<el-row :gutter="15">
					<el-col :span="12">
						<el-form-item label="医师学历">
							<el-input v-model="doctorsForm.record" 
										placeholder="请输入医师学历…" autocomplete="off"></el-input>
						</el-form-item>
					</el-col>
					<el-col :span="12">
						<el-form-item label="医师职称">
							<el-input v-model="doctorsForm.job"
										placeholder="请输入医师职称…" autocomplete="off"></el-input>
						</el-form-item>
					</el-col>
				</el-row>
				<el-row :gutter="15">
					<el-col :span="12">
						<el-form-item label="挂号费用">
							<el-input v-model="doctorsForm.total" 
										placeholder="请输入医师挂号费用…" autocomplete="off"></el-input>
						</el-form-item>
					</el-col>
					<el-col :span="12">
						<el-form-item label="所属科室">
							<el-select style="width:100%;" v-model="doctorsForm.officeId" placeholder="请选择科室">
								<el-option label="查看全部" value=""></el-option>
								<el-option v-for="(item, index) in offices" 
									:key="index" :label="item.name" :value="item.id"></el-option>
							</el-select>
						</el-form-item>
					</el-col>
				</el-row>
				<el-form-item label="专长描述">
					<el-input v-model="doctorsForm.good" type="textarea" :rows="6"
							placeholder="请输入医师专长描述…" autocomplete="off"></el-input>
				</el-form-item>
			</el-form>
			<div slot="footer" class="dialog-footer">
				<el-button @click="showAddFlag = false">取 消</el-button>
				<el-button type="primary" @click="addInfo()">确 定</el-button>
			</div>
		</el-dialog>
		
		<el-dialog title="修改信息" width="600px" :visible.sync="showUpdFlag">
			<el-form label-width="90px" :model="doctorsForm">
				<el-row :gutter="15">
					<el-col :span="12">
						<el-form-item label="医师学历">
							<el-input v-model="doctorsForm.record" 
										placeholder="请输入医师学历…" autocomplete="off"></el-input>
						</el-form-item>
					</el-col>
					<el-col :span="12">
						<el-form-item label="医师职称">
							<el-input v-model="doctorsForm.job"
										placeholder="请输入医师职称…" autocomplete="off"></el-input>
						</el-form-item>
					</el-col>
				</el-row>
				<el-row :gutter="15">
					<el-col :span="12">
						<el-form-item label="挂号费用">
							<el-input v-model="doctorsForm.total" 
										placeholder="请输入医师挂号费用…" autocomplete="off"></el-input>
						</el-form-item>
					</el-col>
					<el-col :span="12">
						<el-form-item label="所属科室">
							<el-select style="width:100%;" v-model="doctorsForm.officeId" placeholder="请选择科室">
								<el-option label="查看全部" value=""></el-option>
								<el-option v-for="(item, index) in offices" 
									:key="index" :label="item.name" :value="item.id"></el-option>
							</el-select>
						</el-form-item>
					</el-col>
				</el-row>
				<el-form-item label="专长描述">
					<el-input v-model="doctorsForm.good" type="textarea" :rows="6"
							placeholder="请输入医师专长描述…" autocomplete="off"></el-input>
				</el-form-item>
			</el-form>
			<div slot="footer" class="dialog-footer">
				<el-button @click="showUpdFlag = false">取 消</el-button>
				<el-button type="primary" @click="updInfo()">确 定</el-button>
			</div>
		</el-dialog>
    </div>
</template>

<script>
import { 
	getAllOffices,
	getPageDoctors,
	addDoctors,
	updDoctors,
	delDoctors 
} from '../../api/index.js';

export default {
    data(){

        return {
			offices: [],
			pageInfos: [],
			pageIndex: 1,
			pageSize: 10,
			pageTotal: 0,
			totalInfo: 0,
			loading: true,
			showAddFlag: false,
			showUpdFlag: false,
			doctorsForm: {
				id: "",
				userName: "",
				passWord: "",
				name: "",
				gender: "",
				age: "",
				phone: "",
				type: 1,
				record: "",
				job: "",
				good: "",
				total: "",
				officeId: "",
			},
			qryForm: {
				name: "",
				phone: "",
				record: "",
				job: "",
			},
        }
    },
    methods: {
		
		getPageInfo(pageIndex, pageSize) {
		
			getPageDoctors(pageIndex, pageSize, this.qryForm.name, 
								this.qryForm.phone, this.qryForm.record, this.qryForm.job).then(resp => {

				this.pageInfos = resp.data.data;
				this.pageIndex = resp.data.pageIndex;
				this.pageSize = resp.data.pageSize;
				this.pageTotal = resp.data.pageTotal;
				this.totalInfo = resp.data.count;

				this.loading = false;
			});
		},
		handleSizeChange(pageSize){
		
			this.getPageInfo(1, pageSize);
		},
		handleCurrentChange(pageIndex){

			this.getPageInfo(pageIndex, this.pageSize);
		},
		showAddWin() {

			this.doctorsForm = {
				id: "",
				userName: "",
				passWord: "",
				name: "",
				gender: "",
				age: "",
				phone: "",
				type: 1,
				record: "",
				job: "",
				good: "",
				total: "",
				officeId: "",
			};

			this.showAddFlag = true;
		},
		showUpdWin(row) {

			this.doctorsForm = row;
			this.showUpdFlag = true;
		},
		addInfo() {

			addDoctors(this.doctorsForm).then(resp => {

				this.$message({
					message: resp.msg,
					type: 'success'
				});

				this.getPageInfo(1, this.pageSize);

				this.showAddFlag = false;
			});
		},
		updInfo() {

			updDoctors(this.doctorsForm).then(resp => {

				this.$message({
					message: resp.msg,
					type: 'success'
				});

				this.getPageInfo(1, this.pageSize);

				this.showUpdFlag = false;
			});
		},
		delInfo(id) {

			this.$confirm('即将删除相关信息, 是否继续?', '提示', {
				confirmButtonText: '确定',
				cancelButtonText: '取消',
				type: 'warning'
			}).then(() => {
				
				delDoctors(id).then(resp => {
						
					if(resp.code == 0){
					
						this.$message({
							message: resp.msg,
							type: 'success'
						});

						this.getPageInfo(1, this.pageSize);
					}else{

						this.$message({
							message: resp.msg,
							type: 'warning'
						});
					}
				});
			});
		}
    },
    mounted(){
		
		getAllOffices().then(resp =>{
			
			this.offices = resp.data;
		});
		
        this.getPageInfo(1, this.pageSize);
    }
}

</script>
