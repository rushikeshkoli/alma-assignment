#Django App for the Assignment
- The project can be built using dockerfile.
- Port 8000 is exposed in docker image.

### Two Routes
```
'/api/result' - to add the new record the DB.
'/api/leaderboard' - to get leaderboard details.
```

## Deployment

- This application is deployed on kubernetes cluster(EKS).
- Any commit to the repository starts the codepipline.
- The codebuild generates docker image and pushes it to the ECR. New image can be updated using deployment.spec in EKS.
- The deployment is exposed using load-balancer service.