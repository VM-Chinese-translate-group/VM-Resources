# VM Resources

本仓库用于存储VMTU需要的资源

⚠️在Gitee/CNB的仓库是[VM-Chinese-translate-group/VM-Resources](https://github.com/VM-Chinese-translate-group/VM-Resources)的镜像仓库⚠️

[Github](https://github.com/VM-Chinese-translate-group/VM-Resources)

[Gitee 镜像](https://gitee.com/Wulian233/vmtu)

[CNB 镜像](https://cnb.cool/VMChineseTranslationGroup/VM-Resources)
## ESA 下载镜像

公开文件地址为 `https://files.vmct.top/vm-resources/<仓库内路径>`。
例如 [VM Metadata](https://files.vmct.top/vm-resources/update/v2/vm-meta.json)。

`main` 上公开文件变更时，GitHub Actions 会上传 `README.md`、`name.json`、`tips.txt`、`resourcepack/` 和 `update/` 到 `oss://vmct-resources/vm-resources/`，然后刷新该目录的 ESA 缓存。也可以手动运行 **Deploy CDN Files** 重传当前 `main`。

上传保留从 Git 移除的历史对象，便于已发布客户端继续下载旧版资源。确需下线文件时，删除对应的 OSS 对象后再刷新 ESA 缓存。
