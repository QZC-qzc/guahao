-- 插入数据
INSERT INTO notices (id, title, detail, put_time) VALUES (3, '关于疫情防护宣传通告', '鉴于当前严峻的疫情形式，为了增强群众防护意识，本周五决定开展社区疫情防护宣传活动，有条件的同事请积极参与', '2022-03-17');
INSERT INTO notices (id, title, detail, put_time) VALUES (4, '五一放假通知', '根据相关规定，本次五一假期放假时间不变，各科室根据实际情况，合理安排。', '2022-03-17');

INSERT INTO offices (id, name, detail, put_time) VALUES (1, '骨科', '外科专业科室,业务包括骨病、肿瘤、小儿畸形等。', '2022-02-21');
INSERT INTO offices (id, name, detail, put_time) VALUES (2, '神经内科', '神经方面二级学科，业务包括脑血管、头痛、癫痫等。', '2022-02-21');
INSERT INTO offices (id, name, detail, put_time) VALUES (3, '妇产科', '外科系统', '2022-02-21');
INSERT INTO offices (id, name, detail, put_time) VALUES (4, '血管外科', '外科系统', '2022-02-21');
INSERT INTO offices (id, name, detail, put_time) VALUES (5, '放疗科', '门诊科室。', '2022-02-21');

INSERT INTO users (id, user_name, pass_word, name, gender, age, phone, create_time, type) VALUES (1, 'admin', 'admin', '张三丰', '女', 45, '90919201', '2022-02-21 12:20:00', 0);
INSERT INTO users (id, user_name, pass_word, name, gender, age, phone, create_time, type) VALUES (17, 'zhoudian', 'zhoudian', '周颠', '男', 34, '90919202', '2022-02-22 20:07:17', 1);
INSERT INTO users (id, user_name, pass_word, name, gender, age, phone, create_time, type) VALUES (18, 'zhaomin', 'zhaomin', '赵敏', '男', 23, '90919203', '2022-02-22 20:08:19', 1);
INSERT INTO users (id, user_name, pass_word, name, gender, age, phone, create_time, type) VALUES (20, 'zhouzhiruo', 'zhouzhiruo', '周芷若', '女', 28, '90919205', '2022-03-17 09:40:58', 1);
INSERT INTO users (id, user_name, pass_word, name, gender, age, phone, create_time, type) VALUES (21, 'dingminjun', 'dingminjun', '丁敏君', '女', 35, '90919206', '2022-03-17 09:42:40', 1);
INSERT INTO users (id, user_name, pass_word, name, gender, age, phone, create_time, type) VALUES (22, 'pengyingyu', 'pengyingyu', '彭莹玉', '男', 45, '90919207', '2022-03-17 09:45:47', 1);
INSERT INTO users (id, user_name, pass_word, name, gender, age, phone, create_time, type) VALUES (23, 'weiyixiao', 'weiyixiao', '韦一笑', '男', 46, '90919208', '2022-03-17 09:47:26', 1);
INSERT INTO users (id, user_name, pass_word, name, gender, age, phone, create_time, type) VALUES (24, 'fanyao', 'fanyao', '范瑶', '男', 47, '90919209', '2022-03-17 09:52:07', 1);
INSERT INTO users (id, user_name, pass_word, name, gender, age, phone, create_time, type) VALUES (25, 'zhuchangling', 'zhuchangling', '朱长龄', '男', 40, '90919210', '2022-03-17 09:54:42', 1);
INSERT INTO users (id, user_name, pass_word, name, gender, age, phone, create_time, type) VALUES (26, 'zhujiuzhen', 'zhujiuzhen', '朱九真', '女', 30, '90919211', '2022-03-17 09:56:05', 1);
INSERT INTO users (id, user_name, pass_word, name, gender, age, phone, create_time, type) VALUES (27, 'zhaoqiang', 'zhaoqiang', '赵强', '男', 35, '90919212', '2022-03-17 09:57:10', 1);
INSERT INTO users (id, user_name, pass_word, name, gender, age, phone, create_time, type) VALUES (28, 'wangbaobao', 'wangbaobao', '王保保', '男', 36, '90919213', '2022-03-17 09:58:08', 1);
INSERT INTO users (id, user_name, pass_word, name, gender, age, phone, create_time, type) VALUES (29, 'xiexun', 'xiexun', '谢逊', '男', 48, '90919214', '2022-03-17 09:59:43', 1);
INSERT INTO users (id, user_name, pass_word, name, gender, age, phone, create_time, type) VALUES (30, 'hanqianye', 'hanqianye', '韩千叶', '男', 48, '90919215', '2022-03-17 10:02:11', 1);
INSERT INTO users (id, user_name, pass_word, name, gender, age, phone, create_time, type) VALUES (31, 'songyuanqiao', 'songyuanqiao', '宋远桥', '男', 45, '90919212', '2022-03-18 10:15:35', 2);

INSERT INTO patients (id, address, card) VALUES (31, '武当山12号', '202903920');

INSERT INTO doctors (id, record, job, good, total, office_id) VALUES (17, '本科', '医师', '从事骨伤医疗三十余载，潜心钻研，擅长于手法整复骨折脱位，尤以报创点穴按摩法治疗骨关节及软组织损伤疾患、骶骼关节损伤、踝关节损伤后遗症、颈椎病、肩凝症、腰三横突症、跟病症等诸症，技能独特，疗效颇佳', 40.0, 1);
INSERT INTO doctors (id, record, job, good, total, office_id) VALUES (18, '本科', '专家', '本科学历，神经内科主任医师。擅长脑血管病（脑梗塞、脑出血等）及各种病因所致的头疼、瘫痪与遗传性、脱鞘性、感染性疾的诊断与治疗', 50.0, 2);
INSERT INTO doctors (id, record, job, good, total, office_id) VALUES (20, '本科', '主治医师', '擅长股骨头坏死、强直性脊柱炎、腰椎间盘突出、颈椎病、膝关节炎等骨科疾病的诊治。', 100.0, 1);
INSERT INTO doctors (id, record, job, good, total, office_id) VALUES (21, '本科', '主治医师', '擅长宫腹腔镜下的子宫、附件手术，精通宫腹腔镜联合COOK导丝介入治疗，尤其对不孕不育的诊断和治疗有独特之处。对产科有丰富的临床经验。', 100.0, 3);
INSERT INTO doctors (id, record, job, good, total, office_id) VALUES (22, '研究生', '主任医师', '擅长妇产科各类手术，如：子宫全切术，子宫次全切除术，阴道前后壁修补，陈旧性会阴裂伤修补，宫外孕等，各种妇科疑难杂症，做到了万例手术无事故', 120.0, 3);
INSERT INTO doctors (id, record, job, good, total, office_id) VALUES (23, '研究生', '主任医师', '对类风湿关节炎、风湿性关节炎、痛风等风湿病临床科研与诊疗颇有研究。擅长治疗关节疼痛、肿胀、活动受限等问题，临床经验丰富。', 120.0, 1);
INSERT INTO doctors (id, record, job, good, total, office_id) VALUES (24, '本科', '主治医师', '擅长偏瘫康复、脊髓损伤康复、植物人促醒康复，临床经验丰富。', 100.0, 2);
INSERT INTO doctors (id, record, job, good, total, office_id) VALUES (25, '本科', '主治医师', '擅长神经系统疾病康复、骨关节病康复、植物人促醒等等疾病', 100.0, 2);
INSERT INTO doctors (id, record, job, good, total, office_id) VALUES (26, '本科', '主治医师', '擅长偏瘫康复等疾病，临床经验丰富', 80.0, 2);
INSERT INTO doctors (id, record, job, good, total, office_id) VALUES (27, '本科', '主治医师', '擅长偏瘫康复、脊髓损伤康复等疾病，临床经验丰富。', 100.0, 2);
INSERT INTO doctors (id, record, job, good, total, office_id) VALUES (28, '本科', '主治医师', '擅长偏瘫康复，临床经验丰富。', 75.0, 2);
INSERT INTO doctors (id, record, job, good, total, office_id) VALUES (29, '研究生', '主任医师', '对神经内科疾病颇有研究，脊髓损伤康复，临床经验丰富。', 150.0, 2);
INSERT INTO doctors (id, record, job, good, total, office_id) VALUES (30, '本科', '主治医师', '擅长内科疾病、股骨头坏死、强直性脊柱炎、腰椎间盘突出、颈椎病、膝关节炎等疾病的诊治。', 100.0, 1);

INSERT INTO registe_logs (id, registe_time, create_time, total, status, doctor_id, patient_id) VALUES (4, '2022-03-19', '2022-03-18', 150.0, 0, 29, 31);
INSERT INTO registe_logs (id, registe_time, create_time, total, status, doctor_id, patient_id) VALUES (5, '2022-03-24', '2022-03-20', 80.0, 0, 26, 31);