package com.jd.alpha.skill.client.entity.request;

import lombok.*;

/**
 * Skill Request 槽位信息
 *
 * @author <b>作者：</b> D.Yang（cdyangyang18@jd.com） <br/>
 * <b>时间：</b> 2017/11/29 15:55 <br/>
 * <b>Copyright (c)</b> 2018 京东智能-版权所有 <br/>
 */
@Getter
@Setter
@ToString
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class SkillRequestSlot {

    /**
     * 槽位名称
     */
    private String name;

    /**
     * 槽值
     */
    private String value;

    /**
     * 是否匹配
     */
    private boolean matched;

    /**
     * 槽位确认类型
     */
    private String confirmResult;

}
