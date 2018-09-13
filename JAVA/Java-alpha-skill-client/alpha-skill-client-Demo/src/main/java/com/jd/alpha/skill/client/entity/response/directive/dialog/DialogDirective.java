package com.jd.alpha.skill.client.entity.response.directive.dialog;

import com.jd.alpha.skill.client.entity.response.directive.Directive;
import lombok.*;

/**
 * 类描述
 *
 * @author <b>作者：</b> D.Yang（cdyangyang18@jd.com） <br/>
 * <b>时间：</b> 2017/11/29 17:24 <br/>
 * <b>Copyright (c)</b> 2018 京东智能-版权所有 <br/>
 */
@Getter
@Setter
@ToString
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class DialogDirective extends Directive {

    private String type;

    private String slotName;

    private String name;

    private String confirmResult;

    private DialogIntent intent;

}